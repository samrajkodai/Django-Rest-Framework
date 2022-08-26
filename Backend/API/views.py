from django.forms.models import model_to_dict
from django.http import JsonResponse
from . models import Product

def api_home(request,*args, **kwargs):
    model_data=Product.objects.all().order_by("?").first()
    data={}
    
    if model_data:
        data=model_to_dict(model_data)
        
    
    return JsonResponse({"message":data})