from .models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import ProductFilter
from .forms import ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


class ProductCreate(CreateView, PermissionRequiredMixin):
    permission_required = ('simpleapp.add_product',)
    raise_exception = True
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('simpleapp.change_product',)
    raise_exception = True
    form_class = ProductForm
    model = Product
    template_name = 'product_edit.html'


class ProductDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_product',)
    raise_exception = True
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
