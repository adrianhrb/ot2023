from django.shortcuts import render

from .forms import JudgeIdentification
from .models import Judge


def index(request):
    return render(request, 'judge/judge.html')


def judge_identification(request):
    if request.method == 'POST':
        form = JudgeIdentification(request.POST)
        if form.is_valid():
            try:
                judge = Judge.objects.get(first_name=form.cleaned_data['first_name'])
            except Judge.DoesNotExist:
                message = 'No existe ningun juez con ese nombre, revisa que lo has introducido correctamente'
                return render(request, 'judge/failed.html', dict(message=message))
            password = form.cleaned_data['password']
            if judge.password == password:
                return render(request, 'judge/polls.html')
        message = 'La contrasenya no coincide'
        return render(request, 'judge/failed.html', dict(message=message))
    else:
        form = JudgeIdentification()
        return render(request, 'judge/identification.html', dict(form=form))


def judge_list(request):
    judges = Judge.objects.all()
    return render(request, 'judge/list.html', dict(judges=judges))


def judge_detail(request, judge_slug):
    judge = Judge.objects.get(slug=judge_slug)
    return render(request, 'judge/detail.html', dict(judge=judge))
