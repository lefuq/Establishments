from django.contrib import admin

from apps.catering.models.establishments import Establishment

@admin.register(Establishment)
class EstAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'photo', 'work_time', 'address',
    )
    readonly_fields = (
        'owner', 'coordinates', 'avg_cost'
    )
