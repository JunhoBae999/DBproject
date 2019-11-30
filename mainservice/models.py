from django.db import models
from django.contrib.auth.models import User

# 연습용 코드입니다!

class Music(models.Model) :
    music_no = models.IntegerField(primary_key=True) #짧은 문자열
    music_title = models.CharField(max_length=45)
    music_composer = models.CharField(max_length = 45)
    music_album = models.CharField(max_length=45)
    music_singer = models.CharField(max_length = 45)
    music_release_date = models.DateTimeField('date published')
    music_genre = models.CharField(max_length= 45) #조금 긴 문자열
    music_image = models.ImageField(upload_to='images/',null=True)
    
    # playtime = models.ForeignKey(Play_log)
    # #models.뭐뭐뭐필드()의 형태입니다.
    #어떤 상황에서 어떤 종류의 데이터를 처리해줄지는
    #admin에다가 등록해줘야합니다.
    def __str__(self) :
        return self.music_title
    ## 대문짝에 title 뜨게하기! 

class Play_list(models.Model) :
     pname = models.CharField(max_length=50,primary_key=True,default='unknowplaylist')
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     music = models.ForeignKey(Music,on_delete=models.CASCADE,blank=True,null=True)
     count = 0
     
     def __str__(self):
      return self.pname

# class Play_log(models.Model) :
#     user_id = models.ForeignKey(User,on_delete = models.CASCADE)
#     music_no = models.ForeignKey(Music,on_delete = models.CASCADE)
#     playtime = models.IntegerField()

# class User_membership(models.Model) :
#     user_id = models.ForeignKey(User,on_delete = models.CASCADE)
#     membership = models.BooleanField()
