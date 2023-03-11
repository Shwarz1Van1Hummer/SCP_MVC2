from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from .form import *
from .models import *
from apps.users.models import Profile


# def view_messages(request):
#     if request.method == 'GET':
#         all_message = Message.objects.all()
#         return render(
#                 request=request,
#                 template_name="main_work/chat.html",
#                 context={
#                     'all_message': all_message
#                 }
#             )
#     else:
#         message = request.POST.get('message')
#         c_message = Message.objects.create(message=message)
#         return redirect('/chat/message/')
#

def create_chat(request):
    if request.method == 'POST':
        email = request.POST['email']
        room = request.POST['room']
        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name=room, email=email)

        except Room.DoesNotExist:
            new_room = Room(room_name=room)
            new_room.save()
            return redirect('room', room_name=room, email=email)

    return render(request, 'main_work/create_chat.html')


def message_view(request, room_name, email):
    # user = request.GET['user']
    # image = request.FILE['image']
    get_room = Room.objects.get(room_name=room_name)

    if request.method == 'POST':
        message = request.POST['message']
        new_message = Message(room=get_room, sender=email, message=message)
        new_message.save()

    get_message = Message.objects.filter(room=get_room)

    context = {
        'messages': get_message,
        "user": email
    }
    return render(
        request,
        'main_work/chat.html',
        context
    )
