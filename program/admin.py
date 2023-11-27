from django.contrib import admin

from .models import MusicStyle, Subject


@admin.register(MusicStyle)
class MusicStyleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'description']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
