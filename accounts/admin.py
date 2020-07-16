from django.contrib import admin

# accounts/admin.py
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# UserAdmin을 상속받아서 ModelAdmin 구현.
class CustomUserAdmin(UserAdmin):
    # 관리자 앱에서 사용자정보 *수정*시  name, email, gender가 나오도록 처리
    UserAdmin.fieldsets[1][1]['fields']=('name', 'email', 'gender')
    # 관리자 앱에서 사용자를 *등록* 할때 name, email, gender 가 추가되도록 처리
    # (기본: username, password1, password2)
    UserAdmin.add_fieldsets += (
        ('추가 정보', {'fields':('name', 'email', 'gender')}),
    )
    # 목록에 나올 field들 
    list_display = ['username', 'name', 'email', 'gender']
    # 수정으로 이동할 링크를 추가할 field들
    list_display_links = ['username', 'name']

admin.site.register(CustomUser, CustomUserAdmin)



