from django.urls import path
from . import views

urlpatterns = [
    path('', views.appeals_list, name='appeals_list'),
    path('create/', views.create_appeal, name='create_appeal'),
    path('edit/<int:pk>/', views.edit_appeal, name='edit_appeal'),
]