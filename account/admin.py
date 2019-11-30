from django.contrib import admin
from .models import Music_user
from django.contrib.auth.admin import UserAdmin   
from django.contrib.auth.models import User  

class MusicInline(admin.StackedInline) :
    model= Music_user
    con_delete=False

class CustomerUserAdmin(UserAdmin):
    inlines = (MusicInline,)



admin.site.unregister(User)
admin.site.register(User,CustomerUserAdmin)

# Register your models here.
