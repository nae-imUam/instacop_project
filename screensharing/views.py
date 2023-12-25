# screensharing/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import ScreenSharingSession

def index(request):
    return render(request, 'screensharing/index.html')

def generate_session(request):
    # Generate a unique session ID
    import uuid
    session_id = str(uuid.uuid4())
    
    # Save the session ID in the database
    ScreenSharingSession.objects.create(session_id=session_id)

    return JsonResponse({'session_id': session_id})

def admin_view(request):
    # Retrieve all active screen sharing sessions
    sessions = ScreenSharingSession.objects.all()

    return render(request, 'screensharing/admin.html', {'sessions': sessions})

def screen_share(request, room_name):
    return render(request, 'screensharing/screen_share.html', {
        'room_name': room_name
    })