import json
from django.shortcuts import render
from .models import CurrencyRate
from django.http import HttpResponse, JsonResponse
import random

# Create your views here.
def index(request):
    return render(request, "game/index.html")

def get_random_object(request):
    yearR = random.randint(2016, 2023)
    monthR = random.randint(1, 12)
    object = CurrencyRate.objects.get(year=yearR, month=monthR)
    rateR = object.rate
    data={
        'year': yearR,
        'month': monthR,
        'rate': rateR
    }
    #print(rateR)

    return JsonResponse(data)