from django.shortcuts import render, redirect
from .models import *


def view_scp_news(request):
    if request.method == "GET":
        all_news = News.objects.all()
        # return redirect('/news/nscp/')
        return render(
            request=request,
            template_name="primary/protect.html",
            context={
                'all_news': all_news
            }
        )
    # else:
    #     return redirect('/scp/add/')


