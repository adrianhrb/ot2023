from django.shortcuts import render

from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'list.html', dict(teachers=teachers, section='profesores'))


def teacher_detail(request, teacher_slug):
    teacher = Teacher.objects.get(slug=teacher_slug)
    subjects = list(teacher.subject.all())
    subjects = ",".join([subject.name for subject in subjects])
    return render(
        request, 'detail.html', dict(teacher=teacher, subject=subjects, section='profesores')
    )
