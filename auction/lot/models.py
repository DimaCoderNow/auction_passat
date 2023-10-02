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
