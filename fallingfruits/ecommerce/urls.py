from django.urls import path
from ecommerce import views

urlpatterns = [
    path('',views.index, name='dashboard'),
]
