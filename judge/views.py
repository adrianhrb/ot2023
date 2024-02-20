from django.shortcuts import render

from .models import Judge


def index(request):
    return render(request, 'judge/judge.html')


def judge_list(request):
    judges = Judge.objects.all()
    return render(request, 'judge/list.html', dict(judges=judges))


def judge_detail(request, judge_slug):
    judge = Judge.objects.get(slug=judge_slug)
    return render(request, 'judge/detail.html', dict(judge=judge))
