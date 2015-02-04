from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question List',    {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
admin.site.register(Poll, PollAdmin)
# Register your models here.
