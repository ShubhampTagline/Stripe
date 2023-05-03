from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http.response import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
import stripe

class stripe_view(TemplateView):
    template_name = "stripe.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] ="Shubham"
        return context
    

@csrf_exempt
def stripe_config(request):
    if request.method == "GET":
        stripe_config = {'public_key': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)
    

@csrf_exempt
def create_checkout_session(request):
    if request.method == "GET":
        domain = "http://" + get_current_site(request).domain
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url =  domain + "sucess?session_id={CHECKOUT_SESSION_ID}",
                cancel_url = domain + 'cancelled/',
                payment_method_type = ['card'],
                mode = 'payment',
                line_items = [
                    {}
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


# https://testdriven.io/blog/django-stripe-tutorial/#user-flow
# https://github.com/testdrivenio/django-stripe-checkout/blob/master/payments/views.py