from django.db import models
from django.conf import settings


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    def __repr__(self):
        return '{0} ({1})'.format(object.__repr__(self), str(self))
