from django.urls import path

from . import views

app_name = 'portfolios'
urlpatterns = [
    #path('', views.Index, name='portfolio_list'),
    path('', views.PortfolioList.as_view(), name='portfolio_list'),
    path('<int:pk>', views.PortfolioView.as_view(), name='portfolio_view'),
    path('<int:pk>/edit', views.PortfolioUpdate.as_view(), name='portfolio_edit'),
    path('<int:pk>/delete', views.PortfolioDelete.as_view(), name='portfolio_delete'),
    path('create', views.PortfolioCreate.as_view(), name='portfolio_new'),
]