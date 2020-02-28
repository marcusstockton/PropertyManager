from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Property
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

	def get_context_data(self, **kwargs):
		data = super(PropertyView, self).get_context_data(**kwargs)
		data["portfolio"] = self.kwargs["portfolio_id"]
		logger.info(data['portfolio'])
		return data


class PropertyCreate(CreateView):
	model = Property
	fields = ['address']
	success_url = reverse_lazy('Property_list')

	def get_context_data(self, **kwargs):
		data = super(PropertyCreate, self).get_context_data(**kwargs)
		return data


class PropertyUpdate(UpdateView):
	model = Property
	fields = ['address']
	success_url = reverse_lazy('Property_list')

	def get_context_data(self, **kwargs):
		data = super(PropertyUpdate, self).get_context_data(**kwargs)
		return data


class PropertyDelete(DeleteView):
	model = Property
	success_url = reverse_lazy('Property_list')

	def get_context_data(self, **kwargs):
		data = super(PropertyDelete, self).get_context_data(**kwargs)
		return data