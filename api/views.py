from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from dashboard.models import Course
from dashboard.serializers import CourseSerializer

# Create your views here.

@api_view(['GET'])
def api_home(request, *args, **kargs):
    res = {
        'message' : 'Hello Mr. Amit'
    }

    return Response(res)

@api_view(['GET'])
def course_list(request:Request, *args, **kwargs):
    res = {}
    data = Course.objects.values()
    print('data = ', data)
    print(args)
    print(kwargs)
    return Response(data)

@api_view(['GET'])
def course_details(request:Request, *args, **kwargs):
    print(request.query_params.values)
    id = kwargs['id']
    course:Course
    try:
        course = Course.objects.get(id = id)
    except ObjectDoesNotExist:
        return Response({})

    serialize_course = CourseSerializer(course, many=False)
    return Response(serialize_course.data)