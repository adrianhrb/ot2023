from django.db import models

from competitor.models import Subject


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    avatar = models.ImageField(upload_to='teacher')
    subject = models.ManyToManyField(Subject)
