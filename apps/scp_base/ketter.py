from django.shortcuts import render, redirect
from apps.scp_base.models import SCPKetter


def add_keter(request):
    if request.method == 'GET':
        return render(
            request=request,
            template_name='primary/protect.html',
            context={}
        )
    else:
        title_object = request.POST.get('title_object')
        description = request.POST.get('description')
        file = request.FILES.get('keter_file')
        scp_keter = SCPKetter.objects.create(title_object=title_object, description=description, image=file)
        return redirect('/news/nscp/')


def keter(request):
    if request.method == "GET":
        scp_keter = SCPKetter.objects.all()
        return render(
            request=request,
            template_name='primary/keter_base.html',
            context={'scp_keter': scp_keter}
        )


def scp_keter(request):
    if request.method == 'GET':
        return render(
            request=request,
            template_name='primary/Keter.html',
            context={}
        )


def delete_keter(request, id):
    keter = SCPKetter.objects.get(pk=id)
    keter.delete()
    return redirect('keter_data')

