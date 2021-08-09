from django.contrib import admin
from .models import Run

class RunAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Run, RunAdmin)