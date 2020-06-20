from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db import transaction, IntegrityError
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import transaction
from .models import Property, Address
from portfolios.models import Portfolio
from .forms import AddressForm, PropertyForm, PropertyDocumentFormSet, PropertyImageFormSet
import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'properties/index.html', {})


class PropertyList(ListView):
    model = Property

    def get_context_data(self, **kwargs):
        data = super(PropertyList, self).get_context_data(**kwargs)
        return data


class PropertyView(DetailView):
    model = Property
    form_class = PropertyForm

    def get_context_data(self, **kwargs):
        data = super(PropertyView, self).get_context_data(**kwargs)
        data["portfolio"] = self.kwargs["portfolio_id"]
        data['address'] = Address.objects.filter(property=data["property"].id).first()

        logger.info(data['portfolio'])
        return data


class PropertyCreate(CreateView):
    model = Property
    form_class = PropertyForm
    success_url = reverse_lazy('portfolios:portfolio_list')

    def get_context_data(self, **kwargs):
        data = super(PropertyCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['address'] = AddressForm(self.request.POST)
            data['images'] = PropertyImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
            data['documents'] = PropertyDocumentFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['address'] = AddressForm()
            data['images'] = PropertyImageFormSet(instance=self.object)
            data['documents'] = PropertyDocumentFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        data = self.get_context_data()
        address = data["address"]
        images = data["images"]
        documents = data['documents']
        with transaction.atomic():
            if form.is_valid() and address.is_valid() and images.is_valid() and documents.is_valid():
                with transaction.atomic():
                    new_address = address.save()
                    new_property = form.save(commit=False)
                    new_property.address_id = new_address.id
                    new_property.save()
                    images.save()
                    documents.save()

        return super(PropertyCreate, self).form_valid(form)


class PropertyUpdate(UpdateView):
    model = Property
    form_class = PropertyForm
    success_url = reverse_lazy('portfolios:portfolio_list')

    def get_context_data(self, **kwargs):
        data = super(PropertyUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['address'] = AddressForm(self.request.POST, instance=self.object)
            data['images'] = PropertyImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
            data['documents'] = PropertyDocumentFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data['address'] = AddressForm(instance=Address.objects.filter(property=self.object.id).first())
            data['images'] = PropertyImageFormSet(instance=self.object)
            data['documents'] = PropertyDocumentFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        data = self.get_context_data()
        address = data["address"]
        images = data["images"]
        documents = data['documents']
        with transaction.atomic():
            if form.is_valid() and address.is_valid() and images.is_valid() and documents.is_valid():
                # Property
                updated_property = form.save()
                # Address
                address.instance = updated_property
                address.save()
                # Images
                images.instance = updated_property
                images.save()
                # Documents
                documents.instance = updated_property
                documents.save()
        return super(PropertyUpdate, self).form_valid(form)


class PropertyDelete(DeleteView):
    model = Property
    success_url = reverse_lazy('properties:property_list')

    def get_context_data(self, **kwargs):
        data = super(PropertyDelete, self).get_context_data(**kwargs)
        return data
