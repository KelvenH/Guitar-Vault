from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('favourite_add/<id>/', views.favourite_add, name='favourite_add'),
]