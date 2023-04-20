from django.urls import path
from .views import stripe_view
from .views import stripe

urlpatterns = [
    path("", stripe_view.as_view(), name="stripe"),
    path("stripe/", stripe, name="stripe_config")
]