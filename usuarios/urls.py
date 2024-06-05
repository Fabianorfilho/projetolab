from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.logar, name='login'),
    path('resetsenha/', views.reset_senha, name='password_reset'),
    path('resetsenha_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]