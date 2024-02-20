from django.shortcuts import render

from competitor.models import Competitor


def saving_competitor(request):
    """
    Saving not as a database concept, but as saving the competitor for beeing eliminated
    """
    nominated_competitors = Competitor.objects.filter(nominated=True)
    return render(request, 'vote/save.html', dict(nominated=nominated_competitors))
