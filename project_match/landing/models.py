from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User

class AppUser(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    is_authenticated = models.BooleanField(default=False)
    firsttime_login = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class AppUserProfile(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='profile')
    sector = models.CharField(max_length=30, blank=True)
    interests = models.TextField(max_length=100, blank=True)

class Project(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=256, blank=False)
    description = models.TextField(max_length=500, blank=False)
    attachments = models.BooleanField()
