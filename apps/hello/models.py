from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image


class Contact(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    bio = models.TextField(null=True, blank=True, max_length=300)
    phone = PhoneNumberField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=30)
    other_contacts = models.TextField(null=True, blank=True, max_length=300)
    photo = models.ImageField(upload_to='%Y%m%d', null=True, blank=True)

    def save(self, force_insert=False, force_update=False, update_fields=True,
             using=None):
        super(Contact, self).save()
        if self.photo:
            filename = self.photo.path
            try:
                image = Image.open(filename)
                image.thumbnail((200, 200), Image.ANTIALIAS)
                image.save(filename)

            except IOError as err:
                print(err)
                self.photo = None
                super(Contact, self).save()
        else:
            self.photo = None
            super(Contact, self).save()
