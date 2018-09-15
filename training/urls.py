from django.urls import path, re_path
from training import views

urlpatterns = [
    path('', views.TrainingView.as_view(), name='train'),
    path('training/', views.TrainingView.as_view(), name='training'),
    path('testing/', views.TestingView.as_view(), name='testing'),
]