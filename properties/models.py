from django.db import models
import os

class Property(models.Model):
    portfolio = models.ForeignKey("portfolios.Portfolio", on_delete=models.CASCADE)
    purchase_date = models.DateField(null=True)
    purchase_value = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Properties"


def property_image_upload_to(instance, filename):
    return 'images/propertyImages/%s/%s' % (instance.property.id, filename)


class PropertyImage(models.Model):
    property = models.ForeignKey("Property", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=property_image_upload_to)

    def __str__(self):
        return self.image.name


def property_docs_upload_to(instance, filename):
    return 'documents/propertyDocs/%s/%s' % (instance.property.id, filename)


class PropertyDocument(models.Model):
    property = models.ForeignKey("Property", on_delete=models.CASCADE)
    document = models.FileField(upload_to=property_docs_upload_to)
    document_type = models.ForeignKey("DocumentType", on_delete=models.CASCADE)
    expiry_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    
    def __str__(self):
        return self.document.name

    def filename(self):
        return os.path.basename(self.document.name)


class DocumentType(models.Model):
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.description

class Address(models.Model):
    property = models.OneToOneField("Property", on_delete=models.CASCADE)
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100, null=True, blank=True)
    line3 = models.CharField(max_length=100, null=True, blank=True)
    post_code = models.CharField(max_length=7)
    town = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return "{0} {1}, {2}".format(self.line1, self.line2, self.line3)

