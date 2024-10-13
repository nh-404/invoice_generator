from django.urls import path
from invoice_generator import views

urlpatterns = [
                        
    path('', views.index, name='index'),
    # path('itemList', views.itemList, name='itemList'),
    path('product', views.add_product, name='add_product')
     
]
