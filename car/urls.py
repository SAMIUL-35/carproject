# urls.py
from django.urls import path
from .views import detail_view, buy_car

urlpatterns = [
    path('car/<int:id>/', detail_view.as_view(), name='detail'),
    path('buy/<int:car_id>/', buy_car, name='buy_car'),
  
]
