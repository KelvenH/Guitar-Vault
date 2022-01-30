from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('favourite_add/<int:id>/', views.favourite_add, name='favourite_add'),
    path('request_guitar/<int:id>/', views.request_guitar,
         name='request_guitar'),
]
