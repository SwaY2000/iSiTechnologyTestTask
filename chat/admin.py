from django.contrib import admin

from chat.models import Thread, Message


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('thread_name', 'id', 'display_participants')
    filter_horizontal = ('participants',)

    def thread_name(self, obj):
        return obj.__str__()

    def display_participants(self, obj):
        return ", ".join(obj.participants.values_list('username', flat=True))

    display_participants.short_description = 'Participants'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_name', 'id', 'sender')

    def message_name(self, obj):
        return obj.__str__()
