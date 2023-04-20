from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http.response import JsonResponse

class stripe_view(TemplateView):
    template_name = "stripe.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] ="Shubham"
        return context
    

@csrf_exempt
def stripe(request):
    if request.method == "GET":
        stripe_config = {'public_key': settings.STRIPE_PUBLIC_KEY}
        print("*"*100)
        print(stripe_config)
        print("*"*100)
        return JsonResponse(stripe_config, safe=False)
    
