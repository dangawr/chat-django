from django.contrib import admin
from .models import Room, Message
from django.contrib.auth.models import User


class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }


class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
