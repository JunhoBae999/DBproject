from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save  
from django.dispatch import receiver
from mainservice.models import Music,Play_list
class Music_user(models.Model) :
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    user_name = models.CharField(max_length=45,blank=True)
    user_email = models.EmailField()
    user_phonenumber=models.CharField(max_length=9)
    user_address = models.TextField()
    user_membership = models.BooleanField(null=True)
    def __str__(self):
        return self.user_name
