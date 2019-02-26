from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class User_account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_account = models.CharField(max_length=200, blank=True)
    instagram_account = models.CharField(max_length=200, blank=True)
    twitter_account = models.CharField(max_length=200, blank=True)
    github_account = models.CharField(max_length=200, blank=True)

    def __str__(self):
    	return self.user.username



@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        User_account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    instance.user_account.save()