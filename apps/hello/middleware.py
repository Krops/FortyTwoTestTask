from apps.hello.models import Notification
from django.http import HttpResponsePermanentRedirect as HRPR
from urlparse import urlparse
from django.contrib.auth.models import User
from fortytwo_test_task import settings
import json


def dumps(value):
    return json.dumps(value, default=lambda o: None)


class WebRequestMiddleware(object):

    def process_response(self, request, response):
        if request.path.endswith('/favicon.ico'):
            return response
        if type(response) == HRPR and settings.APPEND_SLASH:
            new_location = response.get('location', None)
            content_length = response.get('content-length', None)
            if new_location and content_length is '0':
                new_parsed = urlparse(new_location)
                old = (('http', 'https')[request.is_secure()],
                       request.get_host(), '{0}/'.format(request.path),
                       request.META['QUERY_STRING'])
                new = (new_parsed.scheme, new_parsed.netloc,
                       new_parsed.path, new_parsed.query)
                if old == new:
                    return response

        try:
            self.save(request, response)
        except Exception as e:
            print(e)
        return response

    def save(self, request, response):
        if hasattr(request, 'user'):
            user = request.user if type(request.user) == User else None
        else:
            user = None

        meta = request.META.copy()
        meta.pop('QUERY_STRING', None)
        meta.pop('HTTP_COOKIE', None)
        Notification(
            host=request.get_host(),
            path=request.path,
            method=request.method,
            uri=request.build_absolute_uri(),
            status_code=response.status_code,
            user_agent=meta.pop('HTTP_USER_AGENT', None),
            remote_addr=meta.pop('REMOTE_ADDR', None),
            remote_addr_fwd=meta.pop('HTTP_X_FORWARDED_FOR', None),
            meta=None if not meta else dumps(meta),
            cookies=None if not request.COOKIES else dumps(request.COOKIES),
            get=None if not request.GET else dumps(request.GET),
            post=None if not request.POST else dumps(request.POST),
            raw_post=None if not request.POST else request.body,
            is_secure=request.is_secure(),
            is_ajax=request.is_ajax(),
            user=user
        ).save()
