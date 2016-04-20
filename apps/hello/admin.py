from django.contrib import admin
from apps.hello.models import Contact


class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('last name', {'fields': ['last_name']}),
        ('date of birth', {'fields': ['date_of_birth']}),
        ('bio', {'fields': ['bio']}),
        ('contacts', {'fields': ['phone']}),
        ('email', {'fields': ['email']}),
        ('jabber', {'fields': ['jabber']}),
        ('skype', {'fields': ['skype']}),
        ('other_contacts', {'fields': ['other_contacts']}),
        ('photo', {'fields': ['photo']}),
    ]
    list_display = ('name', 'last_name', 'date_of_birth', 'email')
    search_fields = ["name", "last_name"]

admin.site.register(Contact, ContactAdmin)
