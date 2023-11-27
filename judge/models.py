from django.db import models


class Judge(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    job = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to='teacher')
    password = models.CharField(max_length=6)
