import csv

from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование колонки')
    width = models.PositiveIntegerField(verbose_name='Длина колонки')

    class Meta:
        verbose_name = 'Колонка'
        verbose_name_plural = 'Колонки'


class Path(models.Model):
    path = models.CharField(max_length=255, verbose_name='Путь к файлу')

    def get_path(self):
        with open(self.path, 'rt') as csv_file:
            header = []
            table = []
            table_reader = csv.reader(csv_file, delimiter=';')
            for table_row in table_reader:
                if not header:
                    header = {idx: value for idx, value in enumerate(table_row)}
                else:
                    row = {header.get(idx) or 'col{:03d}'.format(idx): value
                           for idx, value in enumerate(table_row)}
                    table.append(row)
        return table

    def set_path(self, new_path):
        self.path = new_path

    def save(self):
        path_exist = Path.objects.exists()
        if path_exist:
            print('Путь уже создан, перезапишите значение пути '
                  'при помощи метода set_path')
        else:
            super(Path, self).save()

    class Meta:
        verbose_name = 'Путь'
        verbose_name_plural = 'Пути'
