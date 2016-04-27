from django.contrib import admin
from apps.hello.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'date_of_birth', 'email')
    search_fields = ["name", "last_name"]

admin.site.register(Contact, ContactAdmin)
