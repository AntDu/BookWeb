from django.contrib import admin

from .models import Users, Authors, Books

admin.site.register(Users)
admin.site.register(Authors)
admin.site.register(Books)