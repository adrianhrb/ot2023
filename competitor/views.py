from django.shortcuts import render

from .models import Competitor


def competitors_list(request):
    active_competitors = Competitor.objects.filter(active=True)
    eliminated_competitors = Competitor.objects.filter(active=False)
    return render(
        request,
        'competitor/list.html',
        dict(
            active_competitors=active_competitors,
            eliminated_competitors=eliminated_competitors,
            section='concursantes',
        ),
    )


def competitor_detail(request, competitor_slug):
    competitor = Competitor.objects.get(slug=competitor_slug)
    return render(
        request, 'competitor/detail.html', dict(competitor=competitor, section='concursantes')
    )
