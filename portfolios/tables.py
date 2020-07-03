import django_tables2 as tables
from django_tables2.utils import A
from .models import Portfolio


class PortfolioTable(tables.Table):
    actions = tables.TemplateColumn(template_name='tables/portfolios/portfolio_list_actions.html',
                                    attrs={"td": {"class": "col-sm-3"}})
    property_count = tables.Column(accessor=A('property_count'),)

    class Meta:
        model = Portfolio
        fields = ("name", "property_count", "actions")
        sequence = ("name", "property_count", "actions")
        empty_text = ("There are no portfolio's yet. Please create a portfolio to create properties against.")
