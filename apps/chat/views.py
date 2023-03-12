from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from .form import *
from .models import *
from apps.users.models import Profile


def create_chat(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']

        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name=room, username=username)

        except Room.DoesNotExist:
            new_room = Room(room_name=room)
            new_room.save()
            return redirect('room', room_name=room, username=username)

    return render(request, 'main_work/create_chat.html')


def message_view(request, room_name, username):
    get_room = Room.objects.get(room_name=room_name)

    if request.method == 'POST':
        message = request.POST['message']
        new_message = Message(room=get_room, sender=username, message=message)
        new_message.save()

    get_message = Message.objects.filter(room=get_room)

    context = {
        "messages": get_message,
        "user": username
    }
    return render(
        request,
        'main_work/chat.html',
        context
    )
