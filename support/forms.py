from django import forms
from . import models

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = "__all__"
        # fields = ['title','content']
        #exclude = ['title'] #title 필드만 빼고 나머지 필드드로로 Form Field를 생성
        widgets = {
            # "writer":forms.HiddenInput(), #화면에 나오게 하지 않게함
            "up_file":forms.FileInput(attrs={"class":"form-control-file"}),
            "up-image":forms.FileInput(attrs={"class":"form-control-file"})
        }