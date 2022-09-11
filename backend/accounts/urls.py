from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('official/', views.OfficialDetailView.as_view(), name='official'),
    path('official/create/', views.OfficialRegisterView.as_view(), name='official_register'),
    path('user/', views.UserDetailView.as_view(), name='user'),
    # path('official/<str:token>/', views.OfficialDetailView.as_view(), name='official_detail'),
]
