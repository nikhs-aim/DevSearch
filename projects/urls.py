from django.urls import path
from .import views



urlpatterns=[
     path('project/<str:pk>',views.single_project,name='projects'),
     path('',views.projects,name='projects'),
]