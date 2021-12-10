from django.urls import path
from . import views
urlpatterns = [
    path('',views.OHM,name='BABTRA'),
    path('Home',views.HOME,name='HOME'),
   
    
]