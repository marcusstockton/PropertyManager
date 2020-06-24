from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Tenant, Notes

def index(request):
    return render(request, 'tenants/index.html', {})


class TenantList(LoginRequiredMixin, ListView):
    model = Tenant

    def get_queryset(self):
        propertyId = self.kwargs['propertyId']
        return Tenant.objects.filter(property__id=propertyId)


class TenantDetail(LoginRequiredMixin, DetailView):
    model = Tenant
    fields = ['first_name', 'last_name', 'title', 'occupation', 'date_of_birth', 'property', 'tenancy_start']

class TenantUpdate(LoginRequiredMixin, UpdateView):
    model = Tenant
    fields = ['first_name', 'last_name', 'title', 'occupation', 'date_of_birth', 'property', 'tenancy_start']

class TenantDelete(LoginRequiredMixin, DeleteView):
    model = Tenant
    success_url = reverse_lazy('tenant-list')

class TenantCreate(LoginRequiredMixin, CreateView):
    model = Tenant
    fields = ['first_name', 'last_name', 'title', 'occupation', 'date_of_birth', 'property', 'tenancy_start']
    success_url = reverse_lazy('tenant-list')
    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        return super().form_valid(form)