from django.contrib import admin

from .models import Project, Service, Squad, Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'uuid')

admin.site.register(Squad)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Subscriber, SubscriberAdmin)
