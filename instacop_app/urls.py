# instacop_app/urls.py
from django.urls import path
from .views import participant_list, add_participant, add_email, add_facebook, add_instagram, add_linkedin, add_snapchat, add_telegram, add_thread, add_tinder, add_twitter, add_whatsapp, home

urlpatterns = [
    path('', home, name='home'),
    path('participants/', participant_list, name='participant_list'),
    path('add_participant/', add_participant, name='add_participant'),
    path('add_email/', add_email, name='add_email'),
    path('add_instagram/', add_instagram, name='add_instagram'),
    path('add_facebook/', add_facebook, name='add_facebook'),
    path('add_whatsapp/', add_whatsapp, name='add_whatsapp'),
    path('add_tinder/', add_tinder, name='add_tinder'),
    path('add_telegram/', add_telegram, name='add_telegram'),
    path('add_thread/', add_thread, name='add_thread'),
    path('add_linkedin/', add_linkedin, name='add_linkedin'),
    path('add_snapchat/', add_snapchat, name='add_snapchat'),
    path('add_twitter/', add_twitter, name='add_twitter'),
    
]
