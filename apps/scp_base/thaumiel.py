from django.shortcuts import render, redirect
from apps.scp_base.models import SCPThaumiel
from django.views.generic import View, TemplateView, ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def add_thaumiel(request):
    if request.method == 'GET':
        return render(
            request=request,
            template_name='primary/protect.html',
            context={}
        )
    else:
        title_object = request.POST.get('title_object')
        description = request.POST.get('description')
        file = request.FILES.get('thaumiel_file')
        scp_thaumiel = SCPThaumiel.objects.create(title_object=title_object, description=description, image=file)
        return redirect('/news/nscp/')


# class ThaumielCreateView(CreateView):
#     model = SCPThaumiel
#     template_name = 'primary/protect.html'
#     fields = ['title_object', 'description', 'image']
#     success_url = reverse_lazy('/news/nscp/')


class ThauInfoView(TemplateView):
    template_name = 'primary/Thaumiel.html'


class ThaumieView(ListView):
    model = SCPThaumiel
    template_name = 'primary/thaumiel_base.html'
    context_object_name = 'scp_thaumiel'


def delete_thaumiel(request, id):
    thaumiel = SCPThaumiel.objects.get(pk=id)
    thaumiel.delete()
    return redirect('thaumiel')
