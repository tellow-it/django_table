# Create your views here.
from urllib import request

from django.http import HttpResponseRedirect
from django.views.generic import ListView

from .forms import TableForm
from .models import Table


class TableView(ListView):
    model = Table
    template_name = 'main/list_table.html'
    paginate_by = 5
    context_object_name = 'table_list'

    def get_context_data(self, **kwargs):
        context = super(TableView, self).get_context_data(**kwargs)
        context['form_filter'] = TableForm()
        return context

    def get_queryset(self):
        column = self.request.GET.get('column')
        condition = self.request.GET.get('condition')
        value = self.request.GET.get('value')
        self.queryset = Table.objects.all()
        print(column)
        print(condition)
        print(value)
        if column is None and condition is None and value is None:
            return Table.objects.all()
        if column == '0' and condition == 'empty':
            return Table.objects.all()
        if column == '1' and condition == 'equal':
            self.queryset = Table.objects.all().filter(name=value)
            return self.queryset
        if column == '1' and condition == 'contains':
            self.queryset = Table.objects.all().filter(name__contains=value)
            return self.queryset
        if column == '1' and (condition != 'equal' or condition != 'contains'):
            return Table.objects.all()
        if column == '2' and condition == 'equal':
            self.queryset = Table.objects.all().filter(numbers=value)
            return self.queryset
        if column == '2' and condition == 'more':
            self.queryset = Table.objects.all().filter(numbers__gt=value)
            return self.queryset
        if column == '2' and condition == 'less':
            self.queryset = Table.objects.all().filter(numbers__lt=value)
            return self.queryset
        if column == '2' and condition == 'contains':
            self.queryset = Table.objects.all().filter(numbers__contains=value)
            return self.queryset
        if column == '3' and condition == 'equal':
            self.queryset = Table.objects.all().filter(distance=value)
            return self.queryset
        if column == '3' and condition == 'more':
            self.queryset = Table.objects.all().filter(distance__gt=value)
            return self.queryset
        if column == '3' and condition == 'less':
            self.queryset = Table.objects.all().filter(distance__lt=value)
            return self.queryset
        if column == '3' and condition == 'contains':
            self.queryset = Table.objects.all().filter(distance__contains=value)
            return self.queryset
        return self.queryset

