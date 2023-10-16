from django.shortcuts import render, redirect
from django_user_agents.utils import get_user_agent
from django.db.models import Max

from auction.settings import MEDIA_URL
from .models import Bid, Photo, ViewsCount
from .forms import BidForm, MessageForm


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def count_views(request):
    ip = get_client_ip(request)
    views_count_instance, created = ViewsCount.objects.get_or_create(ip=ip)
    if not created:
        views_count_instance.views_count += 1
    views_count_instance.save()


def index(request):
    count_views(request)
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        template = 'lot/mobile_template.html'
    else:
        template = 'lot/index.html'
    max_bid = Bid.objects.aggregate(Max('amount'))['amount__max']
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['amount'] >= ((max_bid or 0) + 2000):
                form.save()
            # Опционально, добавьте код для обработки успешного сохранения ставки
            return redirect('index')  # Перенаправьте на эту же страницу после успешной отправки ставки
    else:
        form = BidForm()
    message_form = MessageForm()

    bids = Bid.objects.all()[:3]
    images = Photo.objects.all()

    dead_time_str = "2023,9,11"

    context = {
        'form': form,
        'bids': bids,
        'max_bid': max_bid,
        'photo': images,
        'MEDIA_URL': MEDIA_URL,
        'dead_time_str': dead_time_str,
        'message_form': message_form,
    }
    return render(request, template, context)


def save_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['phone']:
                form.save()
            return redirect('index')
    else:
        return redirect('index')
