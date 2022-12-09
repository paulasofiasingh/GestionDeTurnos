from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('turnos/', views.turnos, name='turnos'),
    path('turnos/<int:id>/', views.detail, name='detail'),
    path('mis_turnos/', views.mis_turnos, name="mis_turnos"),
    path('buscar', views.buscar, name='buscar'),
    path('registro/', views.signup, name='signup'),
    path('sesion/', views.sesion, name='sesion'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion')
]