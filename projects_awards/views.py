from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import NewProfileForm, NewProjectForm
from .models import Profile, Projects
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    current_user = request.user
    projects = Projects.get_projects()
    title = "projects"

    return render(request,'projects/home.html', {"title":title, "projects":projects})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.poster_id = current_user.id
            post.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    return render(request, 'new_post.html', {"form": form})



