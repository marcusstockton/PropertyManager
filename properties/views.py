from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import Property, Address
from portfolios.models import Portfolio
from .forms import AddressForm, PropertyForm, PropertyDocumentFormSet, PropertyImageFormSet
from .tables import PropertyTable
from django.contrib.auth.mixins import LoginRequiredMixin
import logging
from django_tables2 import SingleTableView
import pdb
logger = logging.getLogger(__name__)


@login_required
def index(request):
    return render(request, 'properties/index.html', {})


# @login_required
# def property_list(request, portfolio_id):
#     table = PropertyTable(Property.objects
#                           .filter(portfolio_id=portfolio_id)
#                           .filter(portfolio__user=request.user))

#     return render(request, 'properties/property_list.html', {'table': table})


class PropertyList(SingleTableView, LoginRequiredMixin):
    model = Property
    table_class = PropertyTable

    def get_queryset(self):
        portfolio_id = self.kwargs['portfolio_id']
        qs = Property.objects.filter(portfolio_id=portfolio_id).filter(portfolio__user=self.request.user)
        return qs


class PropertyView(DetailView):
    model = Property
    form_class = PropertyForm

    def get_context_data(self, **kwargs):
        data = super(PropertyView, self).get_context_data(**kwargs)
        logger.info(data)
        return data


class PropertyCreate(CreateView):
    model = Property
    form_class = PropertyForm
    success_url = reverse_lazy('portfolios:portfolio_list')

    def get_context_data(self, **kwargs):
        data = super(PropertyCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            logger.info("POST Data: ", self.request.POST)
            data['address'] = AddressForm(self.request.POST)
            data['images'] = PropertyImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
            data['documents'] = PropertyDocumentFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            logger.info("Data: ", self.object)
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
                    logger.info("Saving a new property atomically")
                    new_address = address.save()
                    new_property = form.save(commit=False)
                    new_property.address_id = new_address.id
                    new_property.save()
                    images.save()
                    documents.save()

        return super(PropertyCreate, self).form_valid(form)

    def get_initial(self):
        portfolio = get_object_or_404(Portfolio, id=self.kwargs.get('portfolio_id'))
        return {
            'portfolio': portfolio,
        }


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
                logger.info("Updating property atomically")
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
