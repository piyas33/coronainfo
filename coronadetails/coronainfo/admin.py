from django.contrib import admin
from .models import WorldWide,CaseswithDate,CasesCountry

# Register your models here.

@admin.register(WorldWide)
class WorldWide(admin.ModelAdmin):
    list_display = ['total','deaths','recovered']
@admin.register(CaseswithDate)
class CaseswithDate(admin.ModelAdmin):
    list_display = ['date','total','deaths','recovered']
@admin.register(CasesCountry)
class CasesCountry(admin.ModelAdmin):
    list_display = ['country','total','deaths','recovered']


