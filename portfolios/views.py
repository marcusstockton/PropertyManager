from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Portfolio
from django.urls import reverse_lazy


def index(request):  # not used, but left in for example
    portfolios = Portfolio.objects.get(pk=1)
    context = {'portfolio_list': portfolios}
    return render(request, 'portfolios/index.html', context)


class PortfolioList(ListView):
    model = Portfolio


class PortfolioView(DetailView):
    model = Portfolio


class PortfolioCreate(CreateView):
    model = Portfolio
    fields = ['name']
    success_url = reverse_lazy('portfolios:portfolio_list')


class PortfolioUpdate(UpdateView):
    model = Portfolio
    fields = ['name']
    success_url = reverse_lazy('portfolios:portfolio_list')


class PortfolioDelete(DeleteView):
    model = Portfolio
    success_url = reverse_lazy('portfolios:portfolio_list')