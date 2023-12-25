# instacop_app/admin.py
from django.contrib import admin
from .models import Participant, Instagram, Facebook, Email, Twitter, Tinder, Snapchat, Thread, WhatsApp, Linkedin, Telegram

admin.site.register(Participant)
admin.site.register(Instagram)
admin.site.register(Facebook)
admin.site.register(Email)
admin.site.register(Twitter)
admin.site.register(Tinder)
admin.site.register(Snapchat)
admin.site.register(Thread)
admin.site.register(WhatsApp)
admin.site.register(Linkedin)
admin.site.register(Telegram)
