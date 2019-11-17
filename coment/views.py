from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from .forms import NameForm
from .models import Name


def get_name(request):

    if request.method == 'POST':

        form = NameForm(request.POST)

        if form.is_valid():
            # Сохранение формы
            form.save()


            # Редирект на ту же страницу
            return HttpResponseRedirect(request.path_info)

    else:
    # метод GET

        form = NameForm()

        # Получение всех имен из БД.
        names = Name.objects.all()

    # И добавляем names в контекст, чтобы плучить к ним доступ в шаблоне
    return render(request, 'coment/name.html', {'form': form, 'names': names})
    
