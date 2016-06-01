from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


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


class Notification(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=1000)
    path = models.CharField(max_length=1000)
    method = models.CharField(max_length=50)
    uri = models.CharField(max_length=2000)
    status_code = models.IntegerField()
    user_agent = models.CharField(max_length=1000, blank=True, null=True)
    remote_addr = models.IPAddressField()
    remote_addr_fwd = models.IPAddressField(blank=True, null=True)
    meta = models.TextField()
    cookies = models.TextField(blank=True, null=True)
    get = models.TextField(blank=True, null=True)
    post = models.TextField(blank=True, null=True)
    raw_post = models.TextField(blank=True, null=True)
    is_secure = models.BooleanField()
    is_ajax = models.BooleanField()
    user = models.ForeignKey(User, blank=True, null=True)
