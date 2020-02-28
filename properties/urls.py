from django.urls import path

from . import views

app_name = 'properties'
urlpatterns = [
    path('<int:portfolio_id>/', views.PropertyList.as_view(), name='property_list'),
    path('<int:portfolio_id>/<int:pk>', views.PropertyView.as_view(), name='property_view'),
    path('<int:portfolio_id>/<int:pk>/edit', views.PropertyUpdate.as_view(), name='property_edit'),
    path('<int:portfolio_id>/<int:pk>/delete', views.PropertyDelete.as_view(), name='property_delete'),
    path('<int:portfolio_id>/create', views.PropertyCreate.as_view(), name='property_new'),
]