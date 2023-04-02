from django.contrib import admin

from main.models import Film, UserFilmRelation

admin.site.register(Film)

admin.site.register(UserFilmRelation)