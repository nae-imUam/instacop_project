# screensharing/urls.py

from django.urls import path
from .views import index, generate_session, admin_view, screen_share

urlpatterns = [
    path('', index, name='index'),
    path('generate_session/', generate_session, name='generate_session'),
    path('admin/', admin_view, name='admin_view'),
    path('screen_share/<str:room_name>/', screen_share, name='screen_share'),
]
