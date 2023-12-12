from django.shortcuts import render
from competitor.models import Competitor
from teacher.models import Teacher
from judge.models import Judge
from django.db.models import Q


def index(request):
    return render(request, 'index.html')

def search(request, tofind: str):
    competitors = set(Competitor.objects.filter(Q(first_name__icontains=tofind) | Q(last_name__icontains=tofind)))
    music_styles = set(Competitor.objects.filter(music_style__name__icontains=tofind))
    teachers = set(Teacher.objects.filter(first_name__icontains=tofind))
    judges = set(Judge.objects.filter(first_name__icontains = tofind))
    return render(request, 'results.html', dict(competitors=competitors, music_styles=music_styles, teachers=teachers, judges=judges))