from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('official/<int:pk>/', views.OfficialDetailView.as_view(), name='official-detail'),
    path('official/create/', views.OfficialRegisterView.as_view(), name='official_register'),
    path('official/', views.OfficialListView.as_view(), name='official_list'),

    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('student/create/', views.StudentRegisterView.as_view(), name='student_register'),
    path('student/', views.StudentListView.as_view(), name='student_list'),

    path('teacher/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher-detail'),
    path('teacher/create/', views.TeacherRegisterView.as_view(), name='teacher_register'),
    path('teacher/', views.TeacherListView.as_view(), name='teacher_list'),

    path('staff/<int:pk>/', views.StaffDetailView.as_view(), name='staff-detail'),
    path('staff/create/', views.StaffRegisterView.as_view(), name='staff_register'),
    path('staff/', views.StaffListView.as_view(), name='staff_list'),

    path('user/', views.UserDetailView.as_view(), name='user'),
    # path('official/<str:token>/', views.OfficialDetailView.as_view(), name='official_detail'),
]
