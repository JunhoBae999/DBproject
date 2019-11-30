from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic.detail import DetailView
from .models import Music_user
class MusicuserView(DetailView) :
    context_object_name = 'Music_user'
    model = User
    template_name = 'mainservice/mypage.html'


# Create your views here.
def signup(request):
    if request.method == 'POST' :
        if request.POST['password1'] == request.POST['password2']:
            try :
                user = User.objects.get(username=request.POST['userid'])
                return render(request,'home.html')
            except :
                user = User.objects.create_user(
                username= request.POST['userid'], password = request.POST['password1'])
                user_name = request.POST["username"]
                user_email = request.POST["email"]
                user_phonenumber = request.POST["phonenumber"]
                user_address = request.POST["address"]
                music_user = Music_user(user=user,user_name=user_name,user_email=user_email,user_phonenumber=user_phonenumber,user_address=user_address)
                music_user.save()
                auth.login(request,user)
                return redirect('home')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST' :
        userid = request.POST['userid']
        password = request.POST['password']
        user = auth.authenticate(request,username=userid,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('home')
        else :
            return render(request,'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request) :
    auth.logout(request)
    return redirect('home')
