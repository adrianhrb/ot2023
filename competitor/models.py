from datetime import datetime

from django.db import models
from django.urls import reverse

from program.models import MusicStyle, Subject


class Competitor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=200)
    birthdate = models.DateField()
    city = models.CharField(max_length=255)
    job = models.CharField(max_length=255, blank=True)
    hobbies = models.CharField(max_length=255, help_text='Add subjects separated with ","')
    avatar = models.ImageField(upload_to='competitor')
    active = models.BooleanField()
    subject = models.ManyToManyField(Subject)
    music_style = models.ManyToManyField(MusicStyle)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_years(self):
        today = datetime.today()
        age = (
            today.year
            - self.birthdate.year
            - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        )
        return age

    def get_absolute_url(self):
        return reverse('concursantes:competitor_detail', args=[self.slug])
