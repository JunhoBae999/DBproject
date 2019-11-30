"""musicservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import mainservice.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainservice.views.home,name='home'),
    path('mainservice/mypage',mainservice.views.mypage,name='mypage'),
    path('account/',include('account.urls')),
    path('mainservice/search',mainservice.views.search,name='search'),
    path('mainservice/<int:music_no>',mainservice.views.detail,name='detail'),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
