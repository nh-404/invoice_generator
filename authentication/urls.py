from django.urls import path
from authentication import views

urlpatterns = [
    

    path('', views.singIn, name='login'),
    path('signup', views.signUp, name='signUp'),
    path('logout', views.logout_user, name='logout'),
    path('forget', views.forget_password, name='forgetPass'),
    
]
