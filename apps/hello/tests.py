# -*- coding: utf-8 -*-
from django.test import TestCase
from apps.hello.models import Contact
import json
from django.core.urlresolvers import reverse


class ContactsViewsTestCase(TestCase):
    fixtures = ['fixture.json']

    def test_index(self):
        "Test our index view contact.html with two contacts and cyrilic"
        cont = Contact.objects.get(id=1)
        cont.last_name = u'Кропива'
        cont.save()
        response = self.client.get(reverse('home:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('object' in response.context)
        self.assertEqual(response.context['object'].pk, 1)
        self.assertContains(response, u'Кропива')
        self.assertNotContains(response, u'Андрей')
        self.assertNotContains(response, 'No Contacts')

    def test_emptydb(self):
        "Test our index view contact.html without contacts"
        Contact.objects.all().delete()
        response = self.client.get(reverse('home:index'))
        self.assertContains(response, 'No Contact')

    def test_fields(self):
        "Test our index view contact.html with required fields from json"
        response = self.client.get(reverse('home:index'))
        with open("apps/hello/fixtures/initial_data.json") as data_file:
            data = json.load(data_file)

        fields = data[1][u'fields']
        print(fields)
        for key, value in fields.iteritems():
            self.assertContains(response, value)
