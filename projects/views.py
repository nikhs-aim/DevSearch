from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Project,Tag
from .forms import ProjectForm,ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProjects,paginateProjects
from django.contrib import messages
from django.urls import reverse



def projects(request):
    projects, search_query = searchProjects(request)
    custom_range,projects=paginateProjects(request,projects,6)



    context={'projects':projects,'search_query':search_query,'custom_range':custom_range}
    return render(request,'projects/projects.html',context)


def single_project(request,pk):
    projectObj=Project.objects.get(id=pk)
    form=ReviewForm()

    if request.method == 'POST':
        form=ReviewForm(request.POST)
        review=form.save(commit=False)
        review.project = projectObj
        review.owner=request.user.profile
        review.save()

        projectObj.getVoteCount
        
        messages.success(request,'Your review was successfully submitted !')
        url = reverse('projects', kwargs={'pk': projectObj.id})
        return redirect(url)

    return render(request,'projects/single_project.html',{'project':projectObj,'form':form})



@login_required(login_url="login")
def createProject(request):
    profile=request.user.profile
    form=ProjectForm(request.POST,request.FILES)

    if request.method == 'POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            return redirect('account')
    context={'form':form}
    return render(request,"projects/project_form.html",context)


@login_required(login_url="login")
def updateProject(request,pk):
    profile=request.user.profile
    project=profile.project_set.get(id=pk)  # only the owner can update
    form=ProjectForm(instance=project)

    if request.method == 'POST':
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    context={'form':form}
    return render(request,"projects/project_form.html",context)


@login_required(login_url="login")
def deleteProject(request,pk):
    profile=request.user.profile
    project=profile.project_set.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('account')
    context={'object':project}
    return render(request,'delete_template.html',context)