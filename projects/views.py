from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

def projects(request):
    projects=Project.objects.all()
    context={'projects':projects}
    return render(request,'projects/projects.html',context)


def single_project(request,pk):
    projectObj=Project.objects.get(id=pk)
    return render(request,'projects/single_project.html',{'project':projectObj})

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
            return redirect('projects')
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
            return redirect('projects')
    context={'form':form}
    return render(request,"projects/project_form.html",context)


@login_required(login_url="login")
def deleteProject(request,pk):
    profile=request.user.profile
    project=profile.project_set.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('projects')
    context={'object':project}
    return render(request,'projects/delete_template.html',context)