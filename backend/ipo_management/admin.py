from django.contrib import admin
from .models import IPO

@admin.register(IPO)
class IPOAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'price_band', 'open_date', 'close_date', 'issue_size', 'status']
