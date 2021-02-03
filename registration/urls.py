from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='home'),

    # User Authentication #
    path('user_login/', views.loginPage, name='login'),
    path('user_register/', views.registerPage, name='register'),
    path('user_logout/', views.logoutUser, name='logout'),
]
