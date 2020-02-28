from django.db import models

# Create your models here.
class Property(models.Model):
    address=models.ForeignKey("Address", on_delete=models.CASCADE)
    portfolio = models.ForeignKey("portfolios.Portfolio", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Properties"



def property_image_upload_to(instance, filename):
    return 'images/propertyImages/%s/%s' % (instance.property.id, filename)

class PropertyImage(models.Model):
    property = models.ForeignKey("Property", on_delete=models.CASCADE)
    image = models.ImageField(upload_to = property_image_upload_to)

    def __str__(self):
        return self.image.url


def property_docs_upload_to(instance, filename):
    return 'images/propertyDocs/%s/%s' % (instance.property.id, filename)

class PropertyDocument(models.Model):
    property = models.ForeignKey("Property", on_delete=models.CASCADE)
    document = models.FileField()


class Address(models.Model):
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100, null=True, blank=True)
    line3 = models.CharField(max_length=100, null=True, blank=True)
    post_code = models.CharField(max_length=7)
    town = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Addresses"


