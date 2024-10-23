from django.urls import path
from invoice_generator import views

urlpatterns = [
                        
    path('', views.customer_info, name='customer_Info'),
    path('invoice', views.index, name='index'),
    path('remove/<int:id>/', views.remove_product, name='remove'),
    path('product', views.add_product, name='add_product')
     
]
