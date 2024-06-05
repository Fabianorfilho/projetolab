from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('solicitar_exames/', views.solicitar_exames, name="solicitar_exames"),
    path('fechar_pedido/', views.fechar_pedido, name='fechar_pedido'),
    path('gerenciar_pedidos/', views.gerenciar_pedidos, name='gerenciar_pedidos'),
    path('cancelar_pedido/<int:id_pedido>', views.cancelar_pedido, name='cancelar_pedido'),
    path('enviar_feedback/', views.enviar_feedback, name='enviar_feedback'),
    path('ver_feedback/', views.ver_feedback, name='ver_feedback'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/usuarios/login'), name='logout'),

]
