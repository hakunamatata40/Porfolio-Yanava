from django.shortcuts import render, get_object_or_404
from .models import Project, Education, Experience, Skill
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    projects = Project.objects.all().order_by('-created_at')[:3]
    skills = Skill.objects.all()
    return render(request, 'home.html', {
        'projects': projects,
        'skills': skills
    })

def about(request):
    education = Education.objects.all().order_by('-end_date')
    experiences = Experience.objects.all().order_by('-end_date')
    skills = Skill.objects.all()
    return render(request, 'about.html', {
        'education': education,
        'experiences': experiences,
        'skills': skills
    })

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects.html', {'projects': projects})

# Dans portfolio/views.py
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    # Récupérer le projet précédent et suivant
    previous_project = Project.objects.filter(created_at__lt=project.created_at).order_by('-created_at').first()
    next_project = Project.objects.filter(created_at__gt=project.created_at).order_by('created_at').first()
    
    return render(request, 'project_detail.html', {
        'project': project,
        'previous_project': previous_project,
        'next_project': next_project
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Envoyer l'email
        send_mail(
            f'Message de {name} depuis votre portfolio',
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        messages.success(request, 'Votre message a été envoyé avec succès!')
    
    return render(request, 'contact.html')