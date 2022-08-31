from django.contrib import admin

# Register your models here.

from ..mascota.models import Vacuna, Mascota

admin.site.register(Vacuna)
admin.site.register(Mascota)
