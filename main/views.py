# Create your views here.
from django.views.generic import ListView

from .models import Table
from .filters import TableFilter


class TableView(ListView):
    model = Table
    template_name = 'main/list_table.html'
    paginate_by = 5
    context_object_name = 'table_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = TableFilter(self.request.GET, queryset=self.get_queryset())
        return context
