from django.shortcuts import render, redirect
from .models import *
from .forms import *
from . import forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "Curso/index.html")

# # input
# def get_queryset(self):
#     if self.request.GET.get("consulta"):
#         consulta= self.request.GET.get("consulta")
#         productos= Producto.objects.filter(nombre__icontains=consulta)
#     else:
#         productos = Producto.objects.all()
#     return productos

@login_required
def productos(request):
    # # consulta=models.Producto.objects.all()
    # consulta=Producto.objects.all()
    # contexto={"productos": consulta}
    # return render(request, "Curso/productos.html", contexto)
    consulta = Producto.objects.all()

    if request.GET.get("consulta"):
        consulta = Producto.objects.filter(nombre__icontains=request.GET.get("consulta"))
    contexto = {"productos": consulta}
    return render(request, "Curso/productos.html", contexto)

@login_required
def productos_form(request):
    if request.method == "POST":
        form= forms.ProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos")
    else: 
        form = forms.ProductosForm()
    return render(request, "Curso/productos_form.html", {"form": form})


@login_required
def productos_delete(request, pk:int):
    consulta= Producto.objects.get(id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("productos")
    return render(request, "Curso/productos_confirm_delete.html", {"object": consulta})


@login_required
def productos_details(request, pk:int):
    consulta= Producto.objects.get(id = pk)
    if request.method == "POST":
        consulta.detail()
        return redirect("productos")
    return render(request, "Curso/productos_details.html", {"object": consulta})


@login_required
def proveedores(request):
    # consulta=models.Proveedor.objects.all()
    consulta= Proveedor.objects.all()
    contexto={"proveedores": consulta}
    return render(request, "Curso/proveedores.html", contexto)


@login_required
def proveedores_form(request):
    if request.method == "POST":
        form= forms.ProveedoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("proveedores")
    else: 
        form = forms.ProveedoresForm()
    return render(request, "Curso/proveedores_form.html", {"form": form})

@login_required
def categoria(request):
  consulta=Categoria.objects.all()
  contexto={"object_list": consulta}
  return render(request, "Curso/categoria.html", contexto)

class CustomLoginView(LoginView):
    authentication_form= CustomAuthenticationForm
    template_name = "Curso/login.html"



def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
            
    else: 
        form = CustomUserCreationForm()
    return render(request, "Curso/register.html", {"form": form})