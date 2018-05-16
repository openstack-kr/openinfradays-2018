from django.shortcuts import render
from django.views.generic import ListView
from .models import ProgramCategory


def index(request):
    return render(request, 'index.html')


def schedule_page(request):
    return render(request, 'schedule.html')


class ProgramList(ListView):
    model = ProgramCategory
    template_name = "program.html"
