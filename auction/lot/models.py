from django.db import models
from django.contrib import admin


class Bid(models.Model):
    user_name = models.CharField(max_length=20, verbose_name="Имя")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ваша ставка")
    phone = models.CharField(max_length=20, verbose_name="Ваш номер")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата ставки")

    class Meta:
        verbose_name = "Ставка"
        verbose_name_plural = "Ставки"
        ordering = ['-amount']


class Photo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=2000)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class ViewsCount(models.Model):
    ip = models.CharField(max_length=100)
    views_count = models.IntegerField(default=1)
    first_view = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Счетчик просмотров"
        verbose_name_plural = "Счетчик просмотров"


class Message(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    text = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


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
