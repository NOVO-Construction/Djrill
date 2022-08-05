try:
    from django.urls import re_path as url
except ImportError:
    try:
        from django.conf.urls import url
    except ImportError:
        from django.conf.urls.defaults import url

from .views import DjrillWebhookView


urlpatterns = [
    url(r'^webhook/$', DjrillWebhookView.as_view(), name='djrill_webhook'),
]
