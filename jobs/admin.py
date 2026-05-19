from django.contrib import admin
from .models import Job, Application


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'city', 'salary', 'status')
    list_filter = ('status', 'city')
    search_fields = ('title', 'company', 'city')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'get_company', 'cv', 'short_motivation', 'applied_at')
    list_filter = ('job', 'applied_at')
    search_fields = ('user__username', 'job__title', 'job__company', 'motivation_letter')

    def get_company(self, obj):
        return obj.job.company

    def short_motivation(self, obj):
        if obj.motivation_letter:
            return obj.motivation_letter[:50] + "..."
        return "No motivation letter"

    get_company.short_description = 'Company'
    short_motivation.short_description = 'Motivation Letter'


admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)