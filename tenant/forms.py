from django import forms
from .models import Tenant
from properties.models import Property


class TenantCreateForm(forms.ModelForm): 
    class Meta: 
        model = Tenant
        fields = '__all__'
        widgets = {
            'tenancy_start': forms.DateInput(attrs={'type':'date', 'placeholder':'Select the tenancy start date'}),
            'tenancy_end': forms.DateInput(attrs={'type':'date', 'placeholder':'Select the tenancy end date. Leave blank if current'}),
            'date_of_birth': forms.DateInput(attrs={'type':'date', 'placeholder':'Select a date of birth'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['property'].queryset = Property.objects.filter(portfolio__user = self.user)