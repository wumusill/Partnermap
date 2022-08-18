from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# 총학생회 class
class Partner(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# 인문대학 class
class PartnerHumanity(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes_humanity', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# 사회과학대학 class
class PartnerSociety(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes_society', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# 자연과학대학 class
class PartnerScience(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes_science', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# 경영대학 class
class PartnerBusiness(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes_business', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# 공과대학 class
class PartnerEngine(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes_engine', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# 전자정보대학 class
class PartnerElec(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes_elec', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# 농업생명환경대학 class
class PartnerFarm(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes_farm', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# 사범대학 class
class PartnerTeacher(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes_teacher', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# 생활과학대학 class
class PartnerLife(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes_life', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# 수의과대학 class
class PartnerVet(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes_vet', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# 약학대학 class
class PartnerMedicine(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes_medicine', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# 의과대학 class
class PartnerDoctor(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes_doctor', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


# 융합학과군 class
class PartnerMixed(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    # 좋아요 관련
    like = models.ManyToManyField(User, related_name='likes_mixed', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name