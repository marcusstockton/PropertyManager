from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Tenant, Notes
from properties.models import Property
from .forms import TenantCreateForm
import logging
logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'tenants/index.html', {})


class TenantList(LoginRequiredMixin, ListView):
    model = Tenant

    def get_queryset(self):
        propertyId = self.kwargs['propertyId']
        logger.info('PropertyId', propertyId)
        return Tenant.objects.filter(property__id=propertyId)


class TenantDetail(LoginRequiredMixin, DetailView):
    model = Tenant
    fields = ['first_name', 'last_name', 'title', 'occupation', 'date_of_birth', 'property', 'tenancy_start']


class TenantUpdate(LoginRequiredMixin, UpdateView):
    model = Tenant
    fields = ['first_name', 'last_name', 'title', 'occupation', 'date_of_birth', 'property', 'tenancy_start']
    success_url = reverse_lazy('tenant-list')
    success_message = 'Tenant successfully updated!!!!'


class TenantDelete(LoginRequiredMixin, DeleteView, SuccessMessageMixin):
    model = Tenant
    success_url = reverse_lazy('tenant-list')
    success_message = 'Tenant successfully deleted!!!!'


class TenantCreate(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    model = Tenant
    form_class = TenantCreateForm
    success_url = reverse_lazy('tenant-list')
    success_message = 'Tenant successfully created!!!!'
    
    def get_form_kwargs(self):
        kwargs = super(TenantCreate, self).get_form_kwargs()
        if hasattr(self, 'object'):
            kwargs.update({'user': self.request.user})
        return kwargs

    def get_initial(self):
        property = get_object_or_404(Property, id=self.kwargs.get('propertyId'))
        return {
            'property':property,
        }
