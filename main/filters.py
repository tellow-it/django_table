import django_filters
from .models import Table


class TableFilter(django_filters.FilterSet):
    CHOICES_COLUMN = (
        ('name', 'Name'),
        ('numbers', 'Numbers'),
        ('distance', 'Distance'),
    )
    CHOICES_CONDITION = (
        ('==', '=='),
        ('>', '>'),
        ('<', '<')
    )
    CHOICES_DATA = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )

    column = django_filters.ChoiceFilter(label='Column', choices=CHOICES_COLUMN, method='filter_by_column')
    condition = django_filters.ChoiceFilter(label='Condition', choices=CHOICES_CONDITION, method='filter_by_condition')
    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES_DATA, method='filter_by_order')

    class Meta:
        model = Table
        fields = ['name', ]

    def filter_by_column(self, queryset, name, value):
        if value == 'Name':
            expression = 'name'
        elif value == 'Distance':
            expression = 'distance'
        else:
            expression = 'numbers'
        return queryset.order_by(expression)

    def filter_by_condtion(self, queryset, name, value):
        if value == '==':
            expression = '=='
        elif value == '>':
            expression = '>'
        else:
            expression = '<'
        return queryset.order_by(expression)

    def filter_by_order(self, queryset, name, value):
        expression = 'data' if value == 'ascending' else '-data'
        return queryset.order_by(expression)
