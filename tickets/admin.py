from django.contrib import admin

from . import models

admin.site.register(models.FilmTicket)
admin.site.register(models.TheaterTicket)
admin.site.register(models.ConcertTicket)

admin.site.register(models.People)
admin.site.register(models.Actor)
admin.site.register(models.Director)
admin.site.register(models.Writer)
admin.site.register(models.Producer)

admin.site.register(models.Language)
admin.site.register(models.Genre)
admin.site.register(models.Country)

admin.site.register(models.Film)
admin.site.register(models.Theater)
admin.site.register(models.Song)
admin.site.register(models.Concert)

admin.site.register(models.Place)

admin.site.register(models.ContactUs)
