from django.shortcuts import render

from busstation.models import Station, Route


class Center:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def route_view(request):
    template = 'stations.html'

    route = request.GET.get('route')
    routes = Route.objects.all()
    context = {
        'routes': routes,
    }

    if route:
        route = routes.get(name=route)
        stations = Station.objects.filter(routes=route)
        center = Center(0, 0)
        for station in stations:
            if station.latitude > center.x:
                center.x = station.latitude
            if station.longitude > center.y:
                center.y = station.longitude
        context['stations'] = stations
        context['center'] = center

    return render(request, template, context)


