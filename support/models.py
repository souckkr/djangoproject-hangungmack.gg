from django.db import models
from accounts.models import CustomUser
from ckeditor_uploader.fields import RichTextUploadingField

# 글 카테고리
# class Category(models.Model):
#     category_code = models.AutoField(primary_key=True)
#     category_name = models.CharField(max_length=200)

#     def __str__(self):
#         return f"{self.category_code}.{self.category_name}"



# 게시물(글)
class Post(models.Model):
    # writer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,null=True, blank = True)
    title = models.CharField(verbose_name='Title', max_length=100)
    content = RichTextUploadingField()
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='CATEGORY', null=True, blank = True)

    #FileField : 업로드된 파일의 경로를 저장할 칼럼
    #pillow 라이브러리 설치 필요
    # upload_to : 파일을 저장할 디렉토리.
    up_file = models.FileField(verbose_name='UPLOAD FILE', upload_to='files', null=True, blank = True)
    #imageField : 업로드도니 이미지파일의 경로를 저장
    up_image = models.ImageField(verbose_name='UPLOAD IMAGE', upload_to='images', null=True, blank = True)

    # #작성일시
    # created_at = models.DateTimeField(verbose_name='DATE & TIME of CREATION', auto_now_add=True)
    # #수정일시
    # update_at = models.DateTimeField(verbose_name='UPDATE DATE', auto_now=True)

 