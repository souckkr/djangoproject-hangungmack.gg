from django import forms
from . import models

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = models.Post
        # fields = "__all__"
        # fields = ['title', 'content']
        exclude = ['post_hit', 'like_users'] # title 필드만 빼고 나머지 필드들로 Form Field를 생성
        widgets = {
            "writer": forms.HiddenInput(),
            "up_file": forms.FileInput(attrs={"class":"form-control-file"}),
            "up_image": forms.FileInput(attrs={"class":"form-control-file"}),
            "title": forms.TextInput(attrs={"class":"form-control", "style":"width:100%"}),
            "content": forms.Textarea(attrs={"class":"form-control", "style":"width:100%; height:200px"}),
        }
        # HiddenInput() : <input type='hidden'>

