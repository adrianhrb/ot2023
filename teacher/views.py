from django.shortcuts import render

from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/list.html', dict(teachers=teachers, section='profesores'))


def teacher_detail(request, teacher_slug):
    teacher = Teacher.objects.get(slug=teacher_slug)
    subjects = list(teacher.subject.all())
    sub = ','.join([sub.name for sub in subjects])
    sub_obj = subjects[0]
    return render(
        request,
        'teacher/detail.html',
        dict(teacher=teacher, subject=sub, sub_obj=sub_obj, section='profesores'),
    )
