from django.contrib import admin
from .models import Residente, Invitado, Staff, Sector
# Register your models here.


admin.site.register(Residente)
admin.site.register(Invitado)
admin.site.register(Staff)
admin.site.register(Sector)