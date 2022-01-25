from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_admin, name='site_admin'),
    path('list/', views.GuitarList.as_view(), name='guitarlist'),
    path('add/', views.add_guitar, name='add_guitar'),
    path('edit/<int:guitar_id>/', views.edit_guitar, name='edit_guitar'),
    path('delete/<int:guitar_id>/', views.delete_guitar, name='delete_guitar'),
]
