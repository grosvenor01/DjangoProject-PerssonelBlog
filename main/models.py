from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
User=get_user_model()
class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic =models.ImageField(upload_to='profile_pic')
    description_profile = models.TextField()
    def __str__(self):
        return self.user.username
class certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titre_blog=models.CharField(max_length=500)
    pic_cerf=models.ImageField(upload_to='certi',default='static/images/work-img.jpg')
    date=models.DateField()
    site=models.CharField(max_length=100)
    description_cerf = models.TextField()
    def __str__(self):
        return self.user.username
class work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titre_work=models.CharField(max_length=200)
    pic=models.ImageField(upload_to='work_pic',default='static/images/work-img.jpg')
    année=models.IntegerField()
    description_work=models.TextField()
    def __str__(self):
        return self.user.username
class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titre_post=models.CharField(max_length=200)
    date=models.DateField()
    module=models.CharField(max_length=100)
    description_post = models.TextField()
    def __str__(self):
        return self.user.username
class skille(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=100)
    pourcentage_connaissance=models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(10)])