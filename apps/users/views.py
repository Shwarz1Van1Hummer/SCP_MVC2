from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, View, ListView
from typing import Any
from apps.users.forms import RegisterUserForm, AvtorizateUser, ProfileUpdateForm
from apps.users.models import CustomUser, CustomUserManager, Profile
from django.contrib.auth import (
    authenticate as dj_auntheficate,
    login as dj_login,
    logout, authenticate, login)
from django.db.models import QuerySet
from django.contrib import messages
from bank.models import Account


class RegisterUser(TemplateView):
    def get(self, request, *args: Any, **kwargs: Any):
        form = RegisterUserForm()
        return render(
            request=request,
            template_name='reg_log/register_scp.html',
            context={'form': form}
        )

    def post(self, request, *args: Any, **kwargs: Any) -> HttpResponse:
        template_name: str = 'reg_log/register_scp.html'
        form = RegisterUserForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                template_name,
                {'form': form,
                 }
            )

        user: CustomUser = form.save()
        email: str = form.cleaned_data['email']
        password: str = form.cleaned_data['password']
        user.email = email
        user.set_password(password)
        user.save()

        user: CustomUser = dj_auntheficate(email=email, password=password)
        if (not user) or (not user.is_active):
            return render(
                request,
                self.template_name
            )
        dj_login(request, user)
        users: QuerySet = CustomUser.objects.filter(**form.cleaned_data)
        return render(
            request,
            'primary/protect.html',
            {'users': users}
        )


class LoginView(FormView):
    template_name = 'reg_log/login.html'
    form_class = AvtorizateUser
    success_url = '/news/nscp/'
    user = CustomUser

    def post(self, request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('nscp')
            else:
                messages.success(request, ('Неправильно введен логин или пароль'))
                return redirect('nscp')


def logout_user(request):
    logout(request)
    messages.success(request, ('Вы разлогинены'))
    return redirect('login')


def profile_avatar_create(request):
    if request == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('nscp')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(
        request=request,
        template_name="primary/protect.html",
        context={
            "p_form": p_form
        }
    )


class ProfileUserView(ListView):
    model = CustomUser
    template_name = 'main_work/profile.html'
    context_object_name = 'profile'



#
# def animationview(request):
#     return render(
#         request=request,
#         template_name='reg_log/next_animation.html'
#     )