from django.shortcuts import render

from django.views.generic import ListView, TemplateView, DetailView
from events.models import Event
# Create your views here.

class HomeView(ListView):
	model = Event
	template_name = 'index.html'

	def get_context_data(self, *args, **kwargs):
		event = Event.objects.all()

class ProgramTemplateView(TemplateView):
	template_name = 'program.html'

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event-detail.html'

    def get_context_data(self, *args, **kwargs):
        event = self.get_object()
        user = self.request.user