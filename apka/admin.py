from django.contrib import admin
from .models import Trip, Task

# admin.site.register(Trip)

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    #fields = ['nazwa_imprezy']
    list_display = ['nazwa_imprezy', 'start_date', 'finish_date', 'instutucja']
    list_filter = ('start_date',)
    search_fields = ('organizator',)

admin.site.register(Task)