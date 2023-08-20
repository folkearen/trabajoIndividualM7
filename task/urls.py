from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/', views.task, name='task'),
    path('task/<typ>', views.task, name='task'),
    path('task/create/<int:id>', views.create, name='create'),
    path('task/detail/<int:id>', views.detail, name='detail'),
    path('task/edit/<int:id>', views.edit, name='edit'),
    path('task/delete/<int:id>', views.delete, name='delete'),
]
