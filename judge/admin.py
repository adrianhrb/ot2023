from django.contrib import admin

from .models import Judge


@admin.register(Judge)
class JudgeAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'slug',
        'job',
        'avatar',
    ]
    prepopulated_fields = {'slug': ['first_name', 'last_name']}
