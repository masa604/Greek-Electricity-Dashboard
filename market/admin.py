from django.contrib import admin
from .models import FutureData

@admin.register(FutureData)
class FutureDataAdmin(admin.ModelAdmin):
    list_display = ('date', 'instrument', 'avg_price', 'scraped_at')
    list_filter = ('instrument', 'date')
    search_fields = ('instrument',)