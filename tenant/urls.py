from django.urls import path

from . import views

app_name = 'tenants'
urlpatterns = [
    path('', views.index, name='index'),
]