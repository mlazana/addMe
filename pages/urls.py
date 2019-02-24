from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index, name='index'),
    path('add/', views.add, name='add'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
 ]
