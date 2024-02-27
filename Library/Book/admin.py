from django.contrib import admin

from .models import Book, Location, Publisher


admin.site.register(Book)
admin.site.register(Location)
admin.site.register(Publisher)