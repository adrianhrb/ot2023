import weasyprint
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

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


def eliminated_pdf(request):
    competitors = Competitor.objects.filter(active=False)
    html = render_to_string('competitor/pdf.html', dict(competitors=competitors))
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=eliminated.pdf'
    weasyprint.HTML(string=html).write_pdf(response)
    return response
