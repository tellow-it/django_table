# Create your views here.
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

    # def get_queryset(self):
    #     if self.request.GET.get:
    #         self.queryset = Table.objects.filter(self.request.GET)
    #     return super().get_queryset()
