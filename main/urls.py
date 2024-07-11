from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('calculator/', views.calculator, name='calc'),
    path('fibonacci/', views.fibonacci, name='fib'),
    path('factorial/', views.factorial, name='fact'),
    path('hello/', views.hello, name='hello')
]