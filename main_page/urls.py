from django.urls import path
from . import views


app_name = "main_page"

urlpatterns = [
    path('', views.index, name='index'),
    path('request/', views.TourRequestView.as_view(), name='request'),
    path('about/', views.about, name='about'),
    path('contact/', views.contacts, name='contact-us'),
    path('search/', views.search, name='search'),
]


