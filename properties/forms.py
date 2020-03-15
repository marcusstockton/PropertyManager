from django.forms import inlineformset_factory, ModelForm
from .models import Property, Address, PropertyImage, PropertyDocument


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


class PropertyForm(ModelForm):
    """ Edit a property """
    class Meta:
        model = Property
        exclude = ()
PropertyAddressFormSet = inlineformset_factory(
    parent_model=Property,
    model=Address,
    form=AddressForm,
    extra=1
)

PropertyDocumentFormSet = inlineformset_factory(
    parent_model=Property,
    model=PropertyDocument,
    form=PropertyDocumentForm,
    extra=1
)
PropertyImageFormSet = inlineformset_factory(
    parent_model=Property,
    model=PropertyImage,
    form=PropertyImageForm,
    extra=1,
)