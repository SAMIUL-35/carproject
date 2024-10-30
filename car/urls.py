# urls.py
from django.urls import path
from .views import detail_View, buy_car

urlpatterns = [
    path('car/<int:id>/', detail_View.as_view(), name='detail'),
    path('buy/<int:car_id>/', buy_car, name='buy_car'),
  
]
