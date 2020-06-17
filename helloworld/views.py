from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


import json
def hello(request):
    return HttpResponse('<h1>hello</h1>')
@csrf_exempt
def LST(request):
    if(request.method=='POST'):
        return HttpResponse(json.dumps([json.loads(request.body)]),content_type='text/json')
