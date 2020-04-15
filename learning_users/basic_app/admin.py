from django.contrib import admin
from basic_app.models import UserProfileInfo
# Register your models here.

## we need to register every models
admin.site.register(UserProfileInfo)
