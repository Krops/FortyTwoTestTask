from django.views.generic.detail import DetailView
from hello.models import Contact


class IndexView(DetailView):
    template_name = 'hello/index.html'

    def get_object(self):
        return Contact.objects.first()
