from django.db import models
from django.urls import reverse

from competitor.models import Subject


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    avatar = models.ImageField(upload_to='teacher')
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("profesores:teacher_detail", args=[self.slug])
