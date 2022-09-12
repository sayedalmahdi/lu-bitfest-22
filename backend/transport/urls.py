from django.urls import path, include
from . import views

app_name = 'transport'

urlpatterns = [
    path('bus/', views.BusInventoryListCreate.as_view(), name='bus-list'),
    path('bus/<int:pk>/', views.BusInventoryDetail.as_view(), name='bus-detail'),
    path('stoppage/', views.StoppageListCreate.as_view(), name='stoppage-list'),
    path('stoppage/<int:pk>/', views.StoppageDetail.as_view(), name='stoppage-detail'),
    path('route/', views.RouteListCreate.as_view(), name='route-list'),
    path('route/<int:pk>/', views.RouteDetail.as_view(), name='route-detail'),
]
