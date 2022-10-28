from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'chat'

urlpatterns = [
    path("", views.index, name="index"),
    path("rooms/<slug:room_name>/", views.room, name="room"),
    path("signin/", views.SignIn.as_view(), name="signin"),
    path("login/", LoginView.as_view(template_name='chat/log_in.html'), name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]
