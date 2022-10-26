from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


class SignIn(CreateView):
    form_class = UserCreationForm
    template_name = 'chat/sign_in.html'
    success_url = reverse_lazy('chat:index')
