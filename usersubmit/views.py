from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView
from el_pagination.views import AjaxListView
from . import forms
from .models import *
from common.decorators import ajax_required

# Create your views here.

class PostListView(AjaxListView):
    context_object_name = "post"
    template_name = "usersubmit/post_grid.html"
    page_template='usersubmit/post_ajax.html'

    def get_queryset(self):
        return Post.objects.all()


@login_required
def ArticleDetailView(request,slug,
    template='usersubmit/post_detail.html',
    page_template='usersubmit/comment/comment_ajax.html' ):
    context = {
       'post' : Post.objects.get(slug=slug),
       'comments':Comment.objects.filter(post__slug=slug ),
       'page_template': page_template,
       'comment_form': forms.CommentForm(),
    }
    if request.is_ajax():
        template = page_template
    return render(request, template, context) 



#class ArticleDetailView(DetailView):
    #model = Post    


@login_required
def postview(request):
    form = forms.PostForm()
    formset = forms.ImageInlineFormSet(queryset=Images.objects.none())

    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        formset=forms.ImageInlineFormSet(request.POST,request.FILES,queryset=Images.objects.none())
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author  = request.user
            post.save()
            form.save_m2m()
            images = formset.save(commit=False)
            for image in images:
                image.article = post
                image.save()
            messages.success(request,'Post added.')
            return HttpResponseRedirect('/postfeeds')
    return render(request,'usersubmit/post_create.html',{'form': form,'formset': formset})     
         

@login_required
def post_edit(request,slug):
    post = get_object_or_404(Post,slug=slug)
    form = forms.PostForm(instance=post)
    formset = forms.ImageInlineFormSet(queryset=form.instance.images_set.all())

    if request.user == post.author:
        if request.method == 'POST':
            form = forms.PostForm(request.POST,instance=post)
            formset = forms.ImageInlineFormSet(request.POST,request.FILES,queryset=form.instance.images_set.all())
            if form.is_valid() and formset.is_valid():
                form.save()
                image_updates = formset.save(commit=False)
                for image in image_updates:
                    image.article=post
                    image.save()
                for image in formset.deleted_objects:
                    image.delete()
                messages.success(request,"your post is edited.")
                return HttpResponseRedirect('/postfeeds')
    return render(request,'usersubmit/post_create.html',{'form':form,'formset':formset}) 


@login_required
def post_remove(request, slug):
   post = get_object_or_404(Post,slug=slug)
   if request.user == post.author:
       post.delete()
   return redirect('profiledetail', username=request.user.username)  
   
@ajax_required
@login_required
@require_POST
def post_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')
    if post_id and action:
        try:
            post = Post.objects.get(id=post_id)
            if action == 'like':
                post.users_like.add(request.user)
            else:
                post.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})

       



@ajax_required
@login_required
@require_POST            
def create_post(request):
    post_id = request.POST.get('id')
    if request.method == 'POST' and post_id:
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
             comment_form = form.save(commit=False)
             comment_form.author  = request.user
             comment_form.post=post_id
             comment_form.save()

             response_data['post'] = comment_form.post
             response_data['body'] = comment_form.body
             response_data['created'] = comment_form.created
             response_data['author'] = comment_form.author.username

             return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )  
        

    



