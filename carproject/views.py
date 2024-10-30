from django.shortcuts import render, get_object_or_404
from car.models import CarModel, BrandModel

def home(request, slug=None):
    data = CarModel.objects.all()
    
    if slug:
        brand = BrandModel.objects.get(slug=slug)
        data = CarModel.objects.filter(brand=brand)

    brands = BrandModel.objects.all()
    
    return render(request, 'home.html', {'data': data, 'brands': brands})
