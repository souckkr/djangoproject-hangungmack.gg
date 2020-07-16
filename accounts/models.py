from django.db import models

# accounts/models.py
# AbstractUser - 기존 기본 User를 확장(상속) 해서 만드는 모델.
# AbstractUser 를 상속 한 뒤 추가 Field들을 정의 한다.
# settings.py에 등록 (AUTH_USER_MODEL 변수)

from django.contrib.auth.models import AbstractUser

# username,password(기존) + name, email, gender
class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ['M', '남성'],  #<option value='M'>남성</option>
        ['F', '여성']
    ]
    name = models.CharField(verbose_name='이름', max_length=100)
    email = models.EmailField(verbose_name="이메일", max_length=100)
    gender = models.CharField(verbose_name="성별", max_length=1,
                             choices=GENDER_CHOICES)


