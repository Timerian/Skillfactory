from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Order, Staff

# Create your views here.


class ProductView(ListView):
    model = Product
    context_object_name = 'products'
    ordering = 'name'


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'


class OrderList(ListView):
    model = Order
    context_object_name = "orders"
    ordering = 'time_in'


class OrderDetail(DetailView):
    model = Order
    context_object_name = "order"


class StaffList(ListView):
    model = Staff
    context_object_name = 'staffs'
    ordering = 'full_name'


class StaffDetail(DetailView):
    model = Staff
    context_object_name = 'staff'
