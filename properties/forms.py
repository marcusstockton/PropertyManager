from django.forms import inlineformset_factory, ModelForm, DateInput
from .models import Property, Address, PropertyImage, PropertyDocument


class DateInput(DateInput):
    input_type = 'date'


class AddressForm(ModelForm):
    """ Edit an Address """
    class Meta:
        model = Address
        exclude = ('property',)


class PropertyImageForm(ModelForm):
    """ Edit a Property Image """
    class Meta:
        model = PropertyImage
        exclude = ('property',)


class PropertyDocumentForm(ModelForm):
    """ Edit a property document """
    class Meta:
        model = PropertyDocument
        exclude = ('property',)
        widgets = {
            'expiry_date': DateInput(),
        }


class PropertyForm(ModelForm):
    """ Edit a property """
    class Meta:
        model = Property
        exclude = ('address'),
        widgets = {
            'purchase_date': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }


PropertyDocumentFormSet = inlineformset_factory(
    parent_model=Property,
    model=PropertyDocument,
    form=PropertyDocumentForm,
    extra=0
)

PropertyImageFormSet = inlineformset_factory(
    parent_model=Property,
    model=PropertyImage,
    form=PropertyImageForm,
    extra=1,
)
