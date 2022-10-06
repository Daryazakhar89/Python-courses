from django.contrib import admin
from .models import MySite


class MySiteAdmin(admin.ModelAdmin):
    list_display = ['photo']
    list_display_links = ['photo']


admin.site.register(MySite, MySiteAdmin)




