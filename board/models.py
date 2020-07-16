from django.db import models
from accounts.models import CustomUser
from config import settings

class Category(models.Model):  # 글 카테고리
    # AutoField: 정수의 자동증가 값을 가지는 Field
    category_code = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.category_code}. {self.category_name}"


class Post(models.Model):  # 게시물(글)을 저장할 모델
    writer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(verbose_name='제목', max_length=100)
    content = models.TextField(verbose_name='내용')
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='분류', null=True, blank=True)
    # FileField: 업로드된 파일의 경로를 저장할 컬럼
    # upload_to: 파일을 저장할 디렉토리. MEDIA_ROOT의 하위 디렉토리를 지정
    up_file = models.FileField(verbose_name='업로드파일', upload_to='files', null=True, blank=True)

    # ImageField: 업로드된 이미지파일의 경로를 저장
    # pillow 라이브러리가 설치되 있어야 한다.
    up_image = models.ImageField(verbose_name='업로드이미지', upload_to='images', null=True, blank=True)


    # 작성 일시
    created_at = models.DateTimeField(verbose_name="작성일시", auto_now_add=True)
    # 수정 일시
    update_at = models.DateTimeField(verbose_name='수정일시', auto_now=True)

    post_hit = models.PositiveIntegerField(default=0)

    # 관계되는 모델을 첫번째 인자에 입력. Django 내 내장된 유저모델을 사용하기 위해 settings.AUTH_USER_MODEL 을 입력.
    # like_users 필드는 리스트의 형태를 띄고 있음. 이는 M:N 관계에 따라, like_users 에 하나의 값만 저장되는게 아니라 여러 값이 저장 될 수 있기 때문임
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')

    # 조회수
    @property
    def update_counter(self):
        self.post_hit = self.post_hit + 1
        self.save()
        return self.post_hit

    def __str__(self):
        return f"{self.pk}. {self.title}"

    class Meta:
        ordering = ['-created_at']
# 댓글
from accounts.models import CustomUser
class Comment(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date= models.DateTimeField(auto_now_add=True)
    comment_contents= models.CharField(max_length=200)
    comment_writer= models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering= ['-id']



