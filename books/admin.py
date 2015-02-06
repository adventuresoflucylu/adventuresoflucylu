from django.contrib import admin
#from books.models import Books, TheBigJob
from books.models import AllBooks, TheBigJob
from django.core.urlresolvers import reverse
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE


class TinyMCEAdmin(admin.ModelAdmin):
	class Media:
		js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

#admin.site.register(Book, TinyMCEAdmin)

class BooksAdmin(admin.ModelAdmin):
        prepopulated_fields = {'number': ('name',)}
        list_display = ('name', 'number', 'datepublished', 'isbn')
        search_fields = ['name']

#admin.site.register(Books, BooksAdmin)
#admin.site.register(AllBooks, BooksAdmin)
admin.site.register(AllBooks, TinyMCEAdmin)
admin.site.register(TheBigJob, BooksAdmin)
#admin.site.unregister(FlatPage)
#admin.site.register(FlatPage, TinyMCEFlatPageAdmin)
