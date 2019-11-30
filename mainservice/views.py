from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from accounts.models import Music_user,User_membership
from django.views.generic.detail import DetailView
from .models import Music,Play_list
from django.http import FileResponse
import os
#모델도 임포트 해줘야합니다
def home(request) :
   return render(request,'home.html')
    
    #템플릿에서 사용할때는 쿼리셋(objects).all()이다!!
    #all 말고 .count()는 데이터 갯수를 반환한다.
    #.fist()는 첫번째 객체, .last()는 마지막 객체를 반환
    #Music.objects는 쿼리셋, 포문에서 쓸라믄 contents.all로 하면 다 담길듯.

def mypage(request) :
    mymusic = Play_list.objects.all()
    membership = User_membership.objects.get(user=Music_user.objects.get(user=request.user))
    return render(request,'mypage.html',{'mymusic':mymusic},{'membership':membership})

def search(request):
    membership = User_membership.objects.get(user=Music_user.objects.get(user=request.user))
    all_music = Music.objects.all()
    kewword = request.GET['search_content']
    result = []
    for object in all_music.filter(music_title=kewword):
        result.append(object)
    for object in all_music.filter(music_singer=kewword):
        result.append(object)   
    return render(request,'search.html',{'result':result},{'memberhsip':membership}) 


def detail(request,music_no):
    music_detail = get_object_or_404(Music,pk = music_no)

    return render(request,'detail.html',{'mdetail':music_detail})

def create(request,music_no):
    selected_music = Music.objects.get(music_no=music_no)
    user_list = Play_list()
    user_list.pname=str(request.user.username)+'의 플레이리스트' + str(music_no) ##pname을 계속 변경시켜야됨. 어차피 music_no가 같으면 같은 취급해도 되니까.
    user_list.user=request.user
    user_list.music=selected_music
    user_list.save()
    return render(request,'mypage.html')

def signout(request,user):
    request.user.delete()
    return render(request,'home.html')

def membershipy(request):
    user_membership = User_membership()
    user_membership.username = str(request.user.username)
    user_membership.user = Music_user.objects.get(user = request.user)
    user_membership.yearly = 1
    user_membership.save()
    return redirect('mypage')

def membershipm(request,):   
    user_membership = User_membership()
    user_membership.username = str(request.user.username)
    user_membership.user = Music_user.objects.get(user = request.user)
    user_membership.monthly = 1
    user_membership.save()
    return redirect('mypage')

####다운로드어케하지,,
def down(request,music_no) :
    item = get_object_or_404(Music,pk=music_no)
    downloaditem = item.music_file
    response = FileResponse(downloaditem)
    return response
    





    
    



