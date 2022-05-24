from django.contrib import admin

# Register your models here.
from .models import AppUser
from .models import AppUserProfile
from .models import Project

admin.site.register(AppUser)
admin.site.register(AppUserProfile)
admin.site.register(Project)