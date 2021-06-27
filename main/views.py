from django.shortcuts import render
from .models import *

def index(requst):
    skills = Skills_description.objects.all()
    summary = Summary_description.objects.all()
    language = Language_description.objects.all()
    work_exp = Work_experience_description.objects.all()
    education = Education_description.objects.all()
    return render(requst, 'main/index.min.html', {'skills': skills, 'summary': summary, 'language': language, 'work_exp':work_exp, 'education':education,})

