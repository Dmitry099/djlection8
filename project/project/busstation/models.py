from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование станции')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    routes = models.ManyToManyField('Route', related_name="stations", verbose_name='Маршруты')

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'


class Route(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование маршрута')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'