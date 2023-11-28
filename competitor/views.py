from django.shortcuts import render

from .models import Competitor


def competitor_list(request):
    competitors_active = Competitor.objects.filter(active=True)
    eliminated_competitors = Competitor.objects.filter(active=False)
    return render(
        request,
        'list.html',
        dict(
            competitors_active=competitors_active,
            eliminated_competitors=eliminated_competitors,
            section='concursantes',
        ),
    )
