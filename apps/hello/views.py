from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from hello.models import Contact, Notification


class IndexView(DetailView):
    template_name = 'hello/index.html'

    def get_object(self):
        return Contact.objects.first()


class RequestView(ListView):
    template_name = 'hello/requests.html'

    def get_queryset(self):
        return Notification.objects.order_by('-pk')[:10]
