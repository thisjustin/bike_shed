from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from apps.bikes.models import Bike, Brand


def index(request):
    bike_list = Bike.objects.order_by('-price')[:50]
    template = loader.get_template('bikes/index.html')
    context = {'bike_list': bike_list}
    return HttpResponse(template.render(context, request))  # here we send query to template


def detail(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    return render(request, 'bikes/detail.html', {'bike': bike})


def create(request):
    brand_list = Brand.objects.all()[:50]
    return render(request, 'bikes/create.html', {'brand_list': brand_list})
