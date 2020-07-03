from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_tables2 import SingleTableView

from .models import Portfolio
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .tables import PortfolioTable


@login_required()
def index(request):  # not used, but left in for example
    portfolios = Portfolio.objects.get(pk=1)
    context = {'portfolio_list': portfolios}
    return render(request, 'portfolios/index.html', context)


class PortfolioList(LoginRequiredMixin, SingleTableView):
    model = Portfolio
    table_class = PortfolioTable

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)


class PortfolioView(LoginRequiredMixin, DetailView):
    model = Portfolio


class PortfolioCreate(LoginRequiredMixin, CreateView):
    model = Portfolio
    fields = ['name']
    success_url = reverse_lazy('portfolios:portfolio_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse_lazy('portfolios:portfolio_list'))


class PortfolioUpdate(LoginRequiredMixin, UpdateView):
    model = Portfolio
    fields = ['name']
    success_url = reverse_lazy('portfolios:portfolio_list')


class PortfolioDelete(LoginRequiredMixin, DeleteView):
    model = Portfolio
    success_url = reverse_lazy('portfolios:portfolio_list')