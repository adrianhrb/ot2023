from django.db import models
from django.urls import reverse


class Judge(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    job = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to='teacher')
    password = models.CharField(max_length=6)

    def __str__(self) -> str:
        return self.first_name

    def get_absolute_url(self):
        return reverse('jueces:detail', args=[self.slug])
