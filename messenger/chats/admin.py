from django.contrib import admin
from .models import Chat, Member, Message


class ChatsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_group')
    list_filter = ['is_group']


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'chat', 'last_msg', 'new_msg')
    list_select_related = ['last_msg', 'user', 'chat']


class MessageAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'chat', 'created_at')
    list_filter = ['chat']


admin.site.register(Chat, ChatsAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Member, MemberAdmin)