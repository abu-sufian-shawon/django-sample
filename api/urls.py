from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home),
    path('courses/', views.course_list),
    path('courses/<str:id>/', views.course_details),
]