from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project



@api_view(['GET'])
def getRoutes(request):

    routes=[
        {'GET':'/api/projects'},
        {'GET':'/api/projects/1'},
        {'POST':'/api/projects/id/vote'},
        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},    # refresh token is used to generate new token as th token as expiry date
        
    ]
    return Response(routes)



@api_view(['GET'])
def getProjects(request):
    projects=Project.objects.all()
    serializer=ProjectSerializer(projects,many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getProject(request,pk):
    projects=Project.objects.get(id=pk)
    serializer=ProjectSerializer(projects,many=False)
    return Response(serializer.data)