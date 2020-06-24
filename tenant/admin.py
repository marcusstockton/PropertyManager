from django.contrib import admin

# Register your models here.
from .models import Tenant, Notes

admin.site.register(Tenant)
admin.site.register(Notes)