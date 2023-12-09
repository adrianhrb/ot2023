from django.shortcuts import render
from competitor.models import Competitor


def index(request):
    return render(request, 'index.html')

def search(request, tofind: str):
    competitors_title = Competitor.objects.filter(first_name__icontains = tofind)
    return render(request, 'results.html', dict(competitors_title=competitors_title))