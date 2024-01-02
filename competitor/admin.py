from django.contrib import admin

from .models import Competitor


@admin.action(description='Eliminate')
def expel_competitor(modeladmin, request, queryset):
    queryset.update(active=False)


@admin.register(Competitor)
class CompetitorAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'slug',
        'birthdate',
        'city',
        'job',
        'hobbies',
        'avatar',
        'active',
    ]
    prepopulated_fields = {'slug': ['first_name', 'last_name']}
    raw_id_fields = ['subject', 'music_style']
    actions = [expel_competitor]
