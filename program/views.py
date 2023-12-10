from django.shortcuts import render
from competitor.models import Competitor
from teacher.models import Teacher
from judge.models import Judge


def index(request):
    return render(request, 'index.html')

def search(request, tofind: str):
    competitors = Competitor.objects.filter(first_name__icontains = tofind)
    music_styles = Competitor.objects.filter(music_style__name__icontains = tofind)
    teachers = Teacher.objects.filter(first_name__icontains=tofind)
    judges = Judge.objects.filter(first_name__icontains = tofind)
    return render(request, 'results.html', dict(competitors=competitors, music_styles=music_styles, teachers=teachers, judges=judges))