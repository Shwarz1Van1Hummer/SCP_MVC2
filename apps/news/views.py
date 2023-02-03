from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView


class ContactListView(ListView):
    paginate_by = 2
    model = News


# def view_scp_news(request):
#     if request.method == "GET":
#         all_news = News.objects.all()
#         paginator = Paginator(all_news, 4)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         return render(
#             request=request,
#             template_name="primary/protect.html",
#             context={
#                 'page_obj': page_obj,
#                 'all_news': all_news
#             }
#         )
def view_scp_news(request):
    contact_list = News.objects.all()
    paginator = Paginator(contact_list, 4) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'primary/protect.html', {'page_obj': page_obj})


def delete_news(request, id):
    news = News.objects.get(pk=id)
    news.delete()
    return redirect('nscp')


