from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# 제휴 Data 전체 class
class PartnerAll(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    college = models.CharField(max_length=15, default='')
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# 총학생회 class
class Partner(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    college = models.CharField(max_length=15, default='')

    def __str__(self):
        return self.name


# 인문대학 class
class PartnerHumanity(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    college = models.CharField(max_length=15, default='')

    def __str__(self):
        return self.name


# 경영대학 class
class PartnerBusiness(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    college = models.CharField(max_length=15, default='')

    def __str__(self):
        return self.name