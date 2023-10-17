from django.contrib import admin
from .models import Bid, Photo, ViewsCount, Message
# Register your models here.


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'phone', 'amount', 'created_at')
    list_filter = ('created_at',)  # Фильтр по времени создания
    search_fields = ('user_name',)  # Поиск по имени пользователя


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_url', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('image_url',)


@admin.register(ViewsCount)
class ViewsCountAdmin(admin.ModelAdmin):
    list_display = ('ip', 'views_count', 'first_view')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'text', 'date_sent')
