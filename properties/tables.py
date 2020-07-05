import django_tables2 as tables
from .models import Property


class PropertyTable(tables.Table):
    actions = tables.TemplateColumn(template_name='tables/properties/property_list_actions.html',
                                    attrs={"td": {"class": "col-sm-3"}})

    class Meta:
        model = Property
        fields = ("purchase_date", "purchase_value", "rental_price", "number_of_rooms", "address", "address.post_code",
                  "address.town", "address.city", "portfolio", "actions")
        empty_text = ("There are no properties against this portfolio yet. Please add in your property / properties.")