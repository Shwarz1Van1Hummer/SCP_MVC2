from django.shortcuts import render, redirect
from .models import *


def view_messages(request):
    if request.method == "GET":
        all_message = Message.objects.all()
        return render(
            request=request,
            template_name="main_work/chat.html",
            context={
                'all_message': all_message
            }
        )
    else:
        message = request.POST.get('message')
        c_message = Message.objects.create(message=message)
        return redirect('/chat/message/')
