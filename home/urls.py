from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/orders/', include('order'.urls)),
    path('api/prodects/', include('prodects.urls')),
    
]