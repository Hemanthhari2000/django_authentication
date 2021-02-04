from django.urls import path

from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.homePage, name='home'),

    # User Authentication #
    path('user_login/', views.loginPage, name='login'),
    path('user_register/', views.registerPage, name='register'),
    path('user_logout/', views.logoutUser, name='logout'),

    path(
        'reset_password/',
        auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset.html"),
        name="reset_password"),
    path(
        'reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(
            template_name="registration/password_reset_sent.html"),
        name='password_reset_done'),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_forms.html"),
        name="password_reset_confirm"),
    path(
        'reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_over.html"),
        name="password_reset_complete"),

    # Dummy path
    path('dummy/', views.dummy, name='dummy'),
]
