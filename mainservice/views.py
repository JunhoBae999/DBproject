from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from account.models import Music_user
from django.views.generic.detail import DetailView
from .models import Music,Play_list
class MusicuserView(DetailView) :
    context_object_name = 'Music_user'
    model = User
    template_name = 'mypage.html'

#모델도 임포트 해줘야합니다
def home(request) :
   return render(request,'home.html')
    
    #템플릿에서 사용할때는 쿼리셋(objects).all()이다!!
    #all 말고 .count()는 데이터 갯수를 반환한다.
    #.fist()는 첫번째 객체, .last()는 마지막 객체를 반환
    #Music.objects는 쿼리셋, 포문에서 쓸라믄 contents.all로 하면 다 담길듯.

def mypage(request) :
    return render(request,'mypage.html')

def search(request):
    all_music = Music.objects.all()
    kewword = request.GET['search_content']
    result = []
    for object in all_music.filter(music_title=kewword):
        result.append(object)
    for object in all_music.filter(music_singer=kewword):
        result.append(object)   
    return render(request,'search.html',{'result':result}) 


def detail(request,music_no):
    music_detail = get_object_or_404(Music,pk = music_no)
    user_list = Play_list(pname=User,user=User,music=Music.music_no)
    user_list.save()
    return render(request,'detail.html',{'mdetail':music_detail})




    
    



