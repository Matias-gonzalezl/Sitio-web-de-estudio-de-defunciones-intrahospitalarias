from django.contrib import admin

from .models import Paciente, Region, Hospital

admin.site.register(Paciente)
admin.site.register(Region)
admin.site.register(Hospital)