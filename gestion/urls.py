from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('turnos/', views.turnos, name='turnos'),
    path('turnos/<int:id>/', views.detail, name='detail'),
    path('buscar', views.buscar, name='buscar'),
    path('<int:id>/update/', views.update, name='update'),
    path('registro/', views.signup, name='signup'),
]