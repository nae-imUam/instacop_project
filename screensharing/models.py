# screensharing/models.py

from django.db import models

class ScreenSharingSession(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
