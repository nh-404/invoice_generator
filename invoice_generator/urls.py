from django.urls import path
from invoice_generator import views

urlpatterns = [
    path('', views.index, name='index'),
]
