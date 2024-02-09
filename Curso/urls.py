from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("productos", views.productos, name="productos"),
    path("productos/form", views.productos_form, name="productos_form"),
    path("proveedores", views.proveedores, name="proveedores"),
    path("proveedores/form", views.proveedores_form, name="proveedores_form"),
    path("categoria", views.categoria, name="categoria"),
    path("producto/delete/<int:pk>/", views.productos_delete, name="productos_confirm_delete"),
    path("producto/details/<int:pk>/", views.productos_details, name="productos_details"),
    path("register", views.register, name="register"),
    path("login", CustomLoginView.as_view() , name="login"),
    path("logout", LogoutView.as_view(template_name= "Curso/logout.html") , name="logout")
    
  

]
