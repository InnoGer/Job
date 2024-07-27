from django.shortcuts import render

from .models import Job
# Create your views here.

def job_list(request):
    jobs = Job.objects.all()  # Récupère toutes les instances de Job depuis la base de données
    return render(request, 'jobs/job_list.html', {'jobs': jobs})  # Renvoie un objet HttpResponse avec le contenu du template 'job_list.html' et le contexte {'jobs': jobs}

def job_list2():
    return