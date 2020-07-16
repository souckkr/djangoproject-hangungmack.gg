from django.db import models
# 썸네일
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from embed_video.fields import EmbedVideoField
from config import settings

# Create your models here.
# class Developer(models.Model):
#     developer_name = models.CharField(verbose_name='developer', max_length=100)
    
#     def __str__(self):
#         return self.developer_name


class Genre_list(models.Model):
    genre_list = models.CharField(verbose_name='genre_list', max_length=100)

    def __str__(self):
        return self.genre_list

class Game(models.Model):
    app_id = models.IntegerField(verbose_name= 'app_id', null=True, blank = True)
    title = models.CharField(verbose_name='title', max_length=100)
    # price = models.IntegerField(verbose_name='price')
    genre = models.CharField(verbose_name='genre', max_length=100)
    developer = models.CharField(verbose_name='developer', max_length=100)
    release_at = models.DateTimeField(verbose_name='release Day') 
    info = models.TextField(verbose_name='info')
    pc_requirements_minimum = models.CharField(verbose_name='pc_requirements_minimum',max_length=1000,null=True, blank=True)
    pc_requirements_recommended = models.CharField(verbose_name='pc_requirements_recommended',max_length=1000,null=True, blank=True)
    mac_requirements_minimum =  models.CharField(verbose_name='mac_requirements_minimum',max_length=1000,null=True, blank=True)   
    mac_requirements_recommended =  models.CharField(verbose_name='mac_requirements_recommended',max_length=1000,null=True, blank=True) 
    linux_requirements_minimum =  models.CharField(verbose_name='linux_requirements_minimum',max_length=1000,null=True, blank=True)   
    linux_requirements_recommended =  models.CharField(verbose_name='linux_requirements_recommended',max_length=1000,null=True, blank=True)
    video = EmbedVideoField(null=True)
    # 썸네일
    thumbnail = ProcessedImageField(
		upload_to = 'thumbnail',					# 저장 위치
		processors = [ResizeToFill(220, 70)], # 사이즈 조정
		format = 'JPEG',					# 최종 저장 포맷
		options = {'quality': 80},
        blank =True)  		# 저장 옵션
    # 게임 퍼블리셔
    steam = models.IntegerField(verbose_name= 'steam', null=True, blank = True)
    origin = models.IntegerField(verbose_name= 'origin', null=True, blank = True)
    uplay = models.IntegerField(verbose_name= 'uplay', null=True, blank = True)
    epic_games = models.IntegerField(verbose_name= 'epic_games', null=True, blank = True)
    drmfree = models.IntegerField(verbose_name= 'drmfree', null=True, blank = True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_game')


    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]

#  댓글
from accounts.models import CustomUser
class Comment(models.Model):
    post= models.ForeignKey(Game, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date= models.DateTimeField(auto_now_add=True)
    comment_contents= models.CharField(max_length=200)
    comment_writer= models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name = 'game_comment_writer')

    class Meta:
        ordering= ['-id']