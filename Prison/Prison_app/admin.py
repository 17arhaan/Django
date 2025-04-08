from django.contrib import admin
from .models import Prisoner

@admin.register(Prisoner)
class PrisonerAdmin(admin.ModelAdmin):
    list_display = ('prisoner_id', 'name', 'age', 'block_number', 'cell_number')
    search_fields = ('name', 'prisoner_id')
    list_filter = ('block_number',)                                                                                                         ~