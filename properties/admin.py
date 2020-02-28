from django.contrib import admin

# Register your models here.
from .models import Property, PropertyDocument, PropertyImage, Address

admin.site.register(Property)
admin.site.register(PropertyDocument)
admin.site.register(PropertyImage)
admin.site.register(Address)