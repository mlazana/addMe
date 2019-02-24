from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=200)
    psw = models.CharField(max_length=200)
    fullName = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    facebook_account = models.CharField(max_length=200)
    instagram_account = models.CharField(max_length=200)
    Twitter_account = models.CharField(max_length=200)
    Github_account = models.CharField(max_length=200)

class Contact(models.Model):
	username_added = models.CharField(max_length=200)


