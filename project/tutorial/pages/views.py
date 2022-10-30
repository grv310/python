from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.


def homePageView(request):
    return HttpResponse("Hello World", content_type="text/plain")
    # return JsonResponse({'mystring': "return this string"})

def debug(request):
    return JsonResponse({'key':"value"})
