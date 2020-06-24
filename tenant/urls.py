from django.urls import path

from .views import TenantList, TenantDetail, TenantDelete, TenantCreate, TenantUpdate


app_name = 'tenants'
urlpatterns = [
    path('', TenantList.as_view(), name='tenant-list'),
    path('<int:pk>/', TenantDetail.as_view(), name='tenant-detail'),
    path('<int:pk>/edit', TenantUpdate.as_view(), name='tenant-update'),
    path('<int:pk>/delete', TenantDelete.as_view(), name='tenant-delete'),
    path('create', TenantCreate.as_view(), name='tenant-create'),
]