from django.urls import path
from . import views as core_views 
urlpatterns = [
    path('',core_views.home, name='home'),
    path('about-me/',core_views.about, name='about-me'),
    path('store/',core_views.store, name='store'),
    
]

