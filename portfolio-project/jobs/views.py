from django.shortcuts import render, get_object_or_404
from .models import Job

def home(request):

    jobs = Job.objects.all

    return render(request, "jobs/home.html", {'jobs':jobs})

def detail(request, job_id):
    job = get_object_or_404(Job, pk = job_id)
    return render(request, "jobs/detail.html", {'job':job})