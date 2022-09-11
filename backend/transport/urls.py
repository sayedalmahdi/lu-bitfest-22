from django.urls import path, include
from . import views

app_name = 'transport'

urlpatterns = [
    path('bus/', views.BusInventoryListCreate.as_view(), name='bus-list'),
    path('bus/<int:pk>/', views.BusInventoryDetail.as_view(), name='bus-detail'),
]
