from django.db import models


# 총학생회 class
class Partner(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name


# 인문대학 class
class PartnerHumanity(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name

# 경영대학 class
class PartnerBusiness(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True)
    content = models.CharField(max_length=300)
    address = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name