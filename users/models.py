from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from django.urls import reverse
import os


# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    sex = models.CharField(max_length=10, choices=(('男', '男'), ('女', '女')), blank=True)
    age = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=20, blank=True)
    bio = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=30, blank=True)
    avatar = ProcessedImageField(upload_to='uploads',
                                 default='uploads/123.jpg',
                                 verbose_name='头像',
                                 # 图片将处理成85x85的尺寸
                                 processors=[ResizeToFill(200, 200)], )
    class Meta(AbstractUser.Meta):
        pass

    def save(self, *args, **kwargs):
        # 当用户更改头像的时候，avatar.name = '文件名'
        # 其他情况下avatar.name = 'upload_to/文件名'
        if len(self.avatar.name.split('/')) == 1:
            # print('before:%s' % self.avatar.name)
            # 用户上传图片时，将avatar.name改为 用户名/文件名
            self.avatar.name = self.username + '/' + self.avatar.name
        super(User, self).save()
        # 调用父类的save()方法后，avatar.name就变成了'upload_to/用户名/文件名'
        # print('after:%s' % self.avatar.name)
        # print('avatar_path: %s' % self.avatar.path)





