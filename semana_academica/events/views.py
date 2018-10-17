from django.shortcuts import render

from django.views.generic import ListView, TemplateView
from events.models import Event
# Create your views here.

class HomeView(ListView):
	model = Event
	template_name = 'index.html'

class ProgramTemplateView(TemplateView):
	template_name = 'program.html'