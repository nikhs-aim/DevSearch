from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def paginateProjects(request,projects,results):
    # page=1  # give the first page of the result (if page=2, then it wil display the next three projects)
    # results=3   # give 3 results per page
    # paginator=Paginator(projects,results)   # create paginator which takes in the page and the result

    # projects=paginator.page(page)
    # how many to appear 

    page=request.GET.get('page') 
    paginator=Paginator(projects,results)   

    try:
        projects=paginator.page(page)
    except PageNotAnInteger:
        page=1
        projects=paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages    # if user goes out of index
        projects=paginator.page(page)


    leftIndex = (int(page)-4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1


    custom_range=range(leftIndex,rightIndex)
    return custom_range,projects

def searchProjects(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )
    return projects, search_query