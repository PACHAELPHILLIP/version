from django import forms


from .models import Post,Images

class PostForm(forms.ModelForm):
    category = forms.ChoiceField(widget=forms.Select,choices=Post.CATEGORY_CHOICES)
    class Meta:
        model = Post
        fields = ('title','category','tags' )
        widgets={"category":forms.Select(attrs={'class':'input-field'}), }  

class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image','body', )

ImageFormset= forms.modelformset_factory(
    Images,
    form=ImageForm,
)       

ImageInlineFormSet = forms.inlineformset_factory(
    Post,
    Images,
    extra=0,
    fields = ('image','body', ),
    formset=ImageFormset,
    min_num=1,
)



