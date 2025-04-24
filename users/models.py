from django.db import models

# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 继承 AbstractUser，获得 username, password, email, first_name, last_name 等字段
    # 添加自定义字段
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="头像")
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name="简介")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

