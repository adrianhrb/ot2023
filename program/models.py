from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class MusicStyle(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
