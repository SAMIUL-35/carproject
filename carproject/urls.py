from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('car/', include('car.urls')),
    path('Brand/', include('Brand.urls')),
    path('comments/', include('comments.urls')),
    path('', views.home, name='home'),
    path('Brand/<slug:slug>/', views.home, name='brand_wise_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
