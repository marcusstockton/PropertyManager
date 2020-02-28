from django.db import models

# Create your models here.
class Tenant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=10)
    occupation = models.CharField(max_length=100)
    tenancy_start = models.DateField()
    tenancy_end = models.DateField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name
        

class Notes(models.Model):
    tenant = models.ForeignKey("Tenant", on_delete=models.CASCADE)
    note = models.CharField(max_length=2000)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now = True)

    class Meta:
        verbose_name_plural = "Notes"