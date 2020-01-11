from django.shortcuts import render

from .models import Field, Path


def table_view(request):
    template = 'table.html'

    path = Path.objects.first()
    fields = Field.objects.all()
    table = path.get_path()
    file_name = path.path.split('/')[:-1]

    if not file_name:
        file_name = path.path

    context = {
        'columns': fields,
        'table': table,
        'csv_file': file_name
    }

    result = render(request, template, context)

    return result
