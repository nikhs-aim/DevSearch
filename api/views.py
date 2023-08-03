from django.http import JsonResponse


def getRoutes(request):

    routes=[
        {'GET':'/api/projects'},
        {'GET':'/api/projects/1'},
        {'POST':'/api/projects/id/vote'},
        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},    # refresh token is used to generate new token as th token as expiry date
        
    ]
    return JsonResponse(routes,safe=False)