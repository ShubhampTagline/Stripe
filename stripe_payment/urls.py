from django.urls import path
from .views import stripe_view
from .views import stripe_config
from .views import create_checkout_session

urlpatterns = [
    path("", stripe_view.as_view(), name="stripe"),
    path("config/", stripe_config, name="stripe_config"),
    path("checkout_session/", create_checkout_session, name="create_checkout_session"),
]