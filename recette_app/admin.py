from django.contrib import admin

# Register your models here.
from .models import Recette, Travail_manuel, Activite

admin.site.register(Recette)
admin.site.register(Travail_manuel)
admin.site.register(Activite)
