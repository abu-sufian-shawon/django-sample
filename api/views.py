from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def api_home(request, *args, **kargs):
    res = {
        'message' : 'Hello Mr. Amit'
    }

    return Response(res)