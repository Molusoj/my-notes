from django.contrib import admin
from .models import Note
# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    '''
        Admin View for Note
    '''
    list_display = ('id', 'title', 'slug', 'date_added')
    list_filter = ('title', 'date_added')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Note, NoteAdmin)
