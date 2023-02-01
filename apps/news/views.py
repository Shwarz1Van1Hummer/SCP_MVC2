from django.shortcuts import render, redirect
from .models import *


def view_scp_news(request):
    if request.method == "GET":
        all_news = News.objects.all()
        return render(
            request=request,
            template_name="primary/protect.html",
            context={
                'all_news': all_news
            }
        )


def delete_news(request, id):
    news = News.objects.get(pk=id)
    news.delete()
    return redirect('nscp')


