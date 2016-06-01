from django.conf.urls import url
from apps.hello.views import IndexView, RequestView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^requests/$', RequestView.as_view(), name='requests'),
]
