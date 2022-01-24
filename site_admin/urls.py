from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_admin, name='site_admin'),
]
