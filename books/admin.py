from django.contrib import admin
from books.models import Book

class TinyMCEAdmin(admin.ModelAdmin):
	class Media:
		js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

#admin.site.register(Book, TinyMCEAdmin)

class BooksAdmin(admin.ModelAdmin):
        prepopulated_fields = {'number': ('name',)}
        list_display = ('name', 'number', 'datepublished', 'isbn')
        search_fields = ['name']

admin.site.register(Book, BooksAdmin)

