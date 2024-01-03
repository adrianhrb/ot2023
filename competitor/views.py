import csv
import datetime

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


def competitors_csv(request):
    competitors = Competitor.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=competitors.csv'
    writer = csv.writer(response)
    headers = [field.name for field in Competitor._meta.get_fields()]
    writer.writerow(headers)
    for competitor in competitors:
        data = []
        for header in headers:
            value = getattr(competitor, header)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d%m%Y')
            data.append(value)
        writer.writerow(data)
    return response
