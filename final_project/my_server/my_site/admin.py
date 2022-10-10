from django.contrib import admin
from .models import MySite


class MySiteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    list_display_links = ['title']
    search_fields = ['content']


admin.site.register(MySite, MySiteAdmin)




