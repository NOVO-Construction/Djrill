from django.urls import path

from .views import DjrillWebhookView

urlpatterns = [
    path("webhook/", DjrillWebhookView.as_view(), name="djrill_webhook"),
]
