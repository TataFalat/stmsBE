from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.orderList, name='orderList'),
    path('order/<int:pk>/', views.orderDetail, name='orderDetail'),
]
