from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from apps.bikes.models import Bike, Brand
from apps.bikes.forms import BikeForm


def index(request):
    bike_list = Bike.objects.order_by('price')[:50]
    template = loader.get_template('bikes/index.html')
    context = {'bike_list': bike_list}
    return HttpResponse(template.render(context, request))  # here we send query to template


def detail(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    return render(request, 'bikes/detail.html', {'bike': bike})


def create(request):
    brand_list = Brand.objects.all()[:50]
    bike_list = Bike.objects.order_by('price')[:50]
    try:
        if request.method == 'POST':
            form = BikeForm(request.POST, request.FILES)
            if form.is_valid():
                brand = get_object_or_404(Brand, name=request.POST['brand'])
                instance = Bike(brand=brand, type=request.POST['_type'], model=request.POST['model'],
                                headline=request.POST['headline'], description=request.POST['description'],
                                size=request.POST['size'], price=request.POST['price'],
                                created_by=request.user, image=request.FILES['image'])
                instance.save()
                return render(request, 'bikes/index.html', {'bike_list': bike_list})
            else:
                return render(request, 'bikes/create.html', {'brand_list': brand_list, 'error': form.errors})
    except Exception as e:
        return render(request, 'bikes/create.html', {'brand_list': brand_list, 'error': e})
    return render(request, 'bikes/create.html', {'brand_list': brand_list})
