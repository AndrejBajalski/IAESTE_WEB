from django.contrib import admin
from internship_app.models import *

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name',)

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    exclude = []

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_filter = (
        'status',
        'internship__company',
        'internship__field',
    )
    search_fields = (
        'candidate__name',
        'candidate__surname',
        'internship__referent_number',
    )
    readonly_fields = ('applied_at',)

@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_filter = ('field', 'company')
    search_fields = ('referent_number', 'company__name')


