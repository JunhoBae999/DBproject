from django.contrib import admin
from .models import Music,Play_list
from accounts.models import Music_user


admin.site.register(Music)
admin.site.register(Play_list)

# Register your models here.

