from django.contrib import admin
from . import models# item/admin.py
from embed_video.admin import AdminVideoMixin

class GameAdmin(AdminVideoMixin, admin.ModelAdmin): 
    list_display = ('title','video') 

admin.site.register(models.Game, GameAdmin)
# admin.site.register(models.Game)
admin.site.register(models.Genre_list)
