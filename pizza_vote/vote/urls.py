from django.urls import path
from . import views

urlpatterns = [
    path('', views.pizza_list, name='pizza_list'),
    path('vote/<int:pizza_id>/', views.vote, name='vote'),
]
