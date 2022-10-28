from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Room, Message
from django.contrib.auth.decorators import login_required


def index(request):
    rooms = Room.objects.all()
    return render(request, "chat/index.html", {'rooms': rooms})


@login_required
def room(request, room_name):
    room = Room.objects.get(slug=room_name)
    messages = reversed(Message.objects.filter(room=room).order_by('-pk')[0:50])
    return render(request, "chat/room.html", {"room": room, 'messages': messages})


class SignIn(CreateView):
    form_class = UserCreationForm
    template_name = 'chat/sign_in.html'
    success_url = reverse_lazy('chat:index')
