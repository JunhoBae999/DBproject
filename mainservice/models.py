from django.db import models
from django.contrib.auth.models import User

class Music(models.Model) :
    music_no = models.IntegerField(primary_key=True) #짧은 문자열
    music_title = models.CharField(max_length=45)
    music_composer = models.CharField(max_length = 45)
    music_album = models.CharField(max_length=45)
    music_singer = models.CharField(max_length=10,default='unknow')
    music_release_date = models.DateTimeField('date published')
    music_genre = models.CharField(max_length= 45) #조금 긴 문자열
    music_image = models.ImageField(upload_to='images/',null=True)
    music_file = models.FileField(upload_to='images/',null=True)
    def __str__(self) :
        return self.music_title

class Play_list(models.Model) :
     pname = models.CharField(max_length=50,primary_key=True,default='unknowplaylist')
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     music = models.ForeignKey(Music,on_delete=models.CASCADE,blank=True,null=True)
     def __str__(self):
      return self.pname


