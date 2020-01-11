import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from busstation.models import Station, Route


class Command(BaseCommand):
    help = 'Load data from files'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        BASE_DIR = os.path.dirname(settings.BASE_DIR)
        file_path = os.path.join(BASE_DIR, 'moscow_bus_stations.csv')
        with open(file_path, 'r') as csvfile:
            station_reader = csv.reader(csvfile, delimiter=';')
            next(station_reader)

            for line in station_reader:
                latitude, longitude, raw_routes, name = (line[3], line[2], line[7],
                                                         line[1])
                station = Station.objects.create(name=name, latitude=latitude, longitude=longitude)
                routes = raw_routes.split(';')
                for route in routes:
                    route = route.strip()
                    route_add = Route.objects.filter(name=route).exists()
                    if not route_add:
                        route_add = Route.objects.create(name=route)
                    station.routes.add(route_add)
                    station.save()
            print('Данные из файла moscow_bus_stations.csv загружены')