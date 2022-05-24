from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User


#By defining proxy = True in the Meta class, we tell django that this model overrides the default 
#user behavior. NOTE: This class will still use the default auth_user tables.
class AppUser(User):

    class Meta:
        proxy = True
        ordering = ('username',)
    
    def custom_user_function():
        pass

class AppUserProfile(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, related_name='profile')
    sector = models.CharField(max_length=30, blank=True)
    interests = models.TextField(max_length=100, blank=True)
    

#These @receiver methods make it so that updating the user will update the AppUserProfile
@receiver(post_save, sender=AppUser)
def create_app_user_profile(sender, instance, created, **kwargs):
    if created:
        AppUserProfile.objects.create(user=instance)

@receiver(post_save, sender=AppUser)
def save_app_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Project(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=256, blank=False)
    description = models.TextField(max_length=500, blank=False)
    attachments = models.BooleanField()
