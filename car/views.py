# views.py
from django.shortcuts import  redirect
from django.contrib.auth.decorators import login_required

from django.views import View
from django.views.generic import DetailView
from django.contrib import messages
from .models import CarModel

class detail_view(DetailView):
    model = CarModel
    template_name = "detail.html"
    pk_url_kwarg = 'id'  



@login_required
def buy_car(request, car_id):
    car = CarModel.objects.get(id=car_id)

    
    if car.quantity > 0:
        car.quantity -= 1
        car.save()

        
        car.purchased_by.add(request.user)

        messages.success(request, f"You have successfully bought {car.name}!")
    else:
        messages.error(request, "Sorry, this car is out of stock.")

    return redirect('profile')