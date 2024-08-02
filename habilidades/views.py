from django.shortcuts import render
from .models import Skill, Program

def skills(request):
    skills = Skill.objects.all()
    programs = Program.objects.all()
    return render(request, 'skills.html', {'skills': skills, 'programs': programs})
