
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
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
	form_class=PropertyForm

	def get_context_data(self, **kwargs):
		data = super(PropertyView, self).get_context_data(**kwargs)
		data["portfolio"] = self.kwargs["portfolio_id"]
		data['address'] = Address.objects.filter(property = data["property"].id)

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
				# Property
				self.object = form.save()
				# Address
				address.instance = self.object
				address.save()
				#Images
				images.instance = self.object
				images.save()
				# Documents
				documents.instance = self.object
				documents.save()

		return super(PropertyCreate, self).form_valid(form)
		

# def property_create(request, portfolio_id):
# 	portfolio = Portfolio.objects.get(pk=portfolio_id)
# 	if request.method == 'POST':
# 		property_form = PropertyForm(request.POST)
# 		address_form = AddressForm(request.POST)
# 		property_images_form = PropertyImageFormSet(request.POST, request.FILES, prefix='images')
# 		property_documents_form = PropertyDocumentFormSet(request.POST, request.FILES, prefix='docs')
# 		if property_form.is_valid() and address_form.is_valid() and property_images_form.is_valid() \
# 				and property_documents_form.is_valid():
# 			# Save Property
# 			new_property = property_form.save(commit=False)
# 			new_property.portfolio = portfolio
# 			new_property.save()

# 			# Save Address
# 			property_address = address_form.save(commit=False)
# 			property_address.property = new_property
# 			property_address.save()
			
# 			# Save images
# 			images = property_images_form.save(commit=False)
# 			images.property = new_property
# 			images.save()

# 			# Save Documents
# 			property_documents_form.save()

# 			messages.add_message(request, messages.SUCCESS, 'Property Added!')
# 			return HttpResponseRedirect(reverse_lazy('properties:property_list'))
# 		else:
# 			messages.error(request, "Error")
# 	else:
# 		property_form = PropertyForm(initial={'portfolio': portfolio})
# 		address_form = AddressForm()
# 		property_images_form = PropertyImageFormSet(prefix='images')
# 		property_documents_form = PropertyDocumentFormSet(prefix='docs')
# 		return render(request, 'properties/property_form.html', {'property': property_form, "address": address_form, "images": property_images_form, "docs": property_documents_form})


class PropertyUpdate(UpdateView):
	model = Property
	fields = ['address']
	success_url = reverse_lazy('properties:property_list')

	def get_context_data(self, **kwargs):
		data = super(PropertyUpdate, self).get_context_data(**kwargs)
		return data


class PropertyDelete(DeleteView):
	model = Property
	success_url = reverse_lazy('properties:property_list')

	def get_context_data(self, **kwargs):
		data = super(PropertyDelete, self).get_context_data(**kwargs)
		return data
