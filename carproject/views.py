# views.py
from django.shortcuts import render
from car.models import CarModel, BrandModel

def home(request):
    
    selected_brand = request.GET.get('brand')

    
    if selected_brand:
        cars = CarModel.objects.filter(brand_id=selected_brand)
    else:
        cars = CarModel.objects.all()

  
    brands = BrandModel.objects.all()

    context = {
        'cars': cars,
        'brands': brands,
        'selected_brand': selected_brand,
    }
    return render(request, 'home.html', context)
