from django.shortcuts import render, redirect
from user.forms import AuthForm, RegisterForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User


def auth_view(request):
    if request.method == 'GET':
        context = {
            'form': AuthForm
        }
        return render(request, 'users/auth.html',context=context)

    if request.method == 'POST' or 'post':
        form = AuthForm(data=request.POST) # data- это параметр который принимает данные формы

        """ Аутентификация пользователя"""
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )
            if user:
                """ Авторизация пользователя"""
                login(request, user) # метод login- это авторизация
                return redirect('/products/')
            else:
                form.add_error('username', 'Попробуй еще раз')

        return render(request, 'users/auth.html', context={'form': form}) # Если данные не прошли валидацию


"""Функция выхода из аккаунта """


def logout_view(request):
    logout(request) # метод для выхода из аккаунта
    return redirect('/products/')


"""Регистарция пользователя"""


def register_view(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }
        return render(request, 'users/register.html', context=context)

    if request.method == 'POST' or 'post':
        form = RegisterForm(data=request.POST)

        """Регистарция пользователя"""

        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 == password2: # Если пароли совпадают
                User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                return redirect('/products/')
            else:
                form.add_error('password1', 'Пароли не совпадают')
        return render(request, 'users/register.html', context={'form': form})