from django.urls import path
from country import views

urlpatterns = [
    path('country', views.country_list, name='country'),
    path('country-detail', views.country_detail, name='country-detail'),
]
