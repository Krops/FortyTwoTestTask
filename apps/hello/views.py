from django.views.generic.detail import DetailView
from hello.models import Contact


class IndexView(DetailView):
    template_name = 'hello/contacts.html'

    def get_object(self):
        try:
            return Contact.objects.first()
        except:
            return None
