from django.contrib import admin

from .models import Specialization, Visit, Patient, Service

admin.site.register(Specialization)
admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(Service)