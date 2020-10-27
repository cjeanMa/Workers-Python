from django.contrib import admin
from .models import Persona, Distrito, Profesion

# Register your models here.

admin.site.register([Persona, Distrito, Profesion])