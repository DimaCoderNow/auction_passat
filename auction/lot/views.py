from django.shortcuts import render, redirect
from django_user_agents.utils import get_user_agent
from django.db.models import Max

from auction.settings import MEDIA_URL
from .models import Bid, Photo
from .forms import BidForm


def index(request):
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

    bids = Bid.objects.all()[:3]
    images = Photo.objects.all()

    dead_time_str = "2023,9,11"

    context = {
        'form': form,
        'bids': bids,
        'max_bid': int(max_bid),
        'photo': images,
        'MEDIA_URL': MEDIA_URL,
        'dead_time_str': dead_time_str,
    }
    return render(request, template, context)
