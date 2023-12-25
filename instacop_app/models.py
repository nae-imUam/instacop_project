# instacop_app/models.py
from django.db import models

class Participant(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Instagram(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Email(models.Model):
    username = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Facebook(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Snapchat(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Thread(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Twitter(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Tinder(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class WhatsApp(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Telegram(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Linkedin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username