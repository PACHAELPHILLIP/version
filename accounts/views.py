from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, UserEditForm,ProfileEditForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib import messages
from usersubmit.models import Post
from accounts.models import Contact
from el_pagination.decorators import page_templates
from common.decorators import ajax_required
from django.views.decorators.http import require_POST
from el_pagination.views import AjaxListView
from actions.models import Action
from actions.utils import create_action


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('accounts/acc_active_email.html', {
                'user':user, 
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your blog account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'accounts/verify.html',)
    
    else:
        form = SignupForm()
    
    return render(request, 'accounts/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request, 'accounts/emailactivated.html',)
    else:
        return render(request, 'accounts/emailerror.html',)




@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Thats it!You have just updated your profile successfully!')
        else:
            messages.error(request, 'Error!Looks like you gave some inappropriate info.')
        return redirect('profiledetail', username=request.user.username) 
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'accounts/user/edit.html', {'user_form': user_form,
                                                 'profile_form': profile_form})



@page_templates((
    ('usersubmit/post_ajax.html', None),
    ('accounts/user/follower.html', 'other_entries_page'),
    ('accounts/user/following.html', 'following'),
    )) 
def userdetail(
        request,username, template='accounts/user/detail.html', extra_context=None):
    context = {
        'user' : User.objects.get(username=username,is_active=True),
        'post':Post.objects.filter( author__username=username ),
        'followers':User.objects.get(username=username).followers.all(),
        'following':User.objects.get(username=username).following.all(),
       
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request,template, context)
'''

'''


@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user,
                                              user_to=user)
                create_action(request.user, 'is following', user)                              
            else:
                Contact.objects.filter(user_from=request.user,
                                       user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'ko'})
    return JsonResponse({'status':'ko'})



class FollowerListView(AjaxListView):
    context_object_name = "follower"
    template_name = "/post_grid.html"
    page_template='usersubmit/post_ajax.html'

    def get_queryset(self):
        return Post.objects.all()



@login_required
def dashboard(request):
    # Display all actions by default
    actions = Action.objects.all().exclude(user=request.user)
    following_ids = request.user.following.values_list('id', flat=True)
    if following_ids:
        # If user is following others, retrieve only their actions
        actions = actions.filter(user_id__in=following_ids).select_related('user', 'user__profile').prefetch_related('target')
    actions = actions[:10]

    return render(request, 'accounts/dashboard.html', {'section': 'dashboard',
                                                      'actions': actions})
