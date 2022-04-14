# Create your views here.
from django.views.generic import ListView

from .models import Table


class TableView(ListView):
    model = Table
    template_name = 'main/list_table.html'
    paginate_by = 5
    context_object_name = 'table_list'
