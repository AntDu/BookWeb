from django.contrib import admin

from mainApp.models import User, Author, Book

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Book, filter_horizontal=('book_to_author',))