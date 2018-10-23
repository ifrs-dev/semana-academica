from django.shortcuts import render

from django.views.generic import ListView, TemplateView, DetailView
from events.models import Event, Registration
# Create your views here.

class HomeView(ListView):
    model = Event
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        #context['experiments'] = Experiment.objects.all()
        context['events'] = Event.objects.all()
        return context

class ProgramTemplateView(TemplateView):
    template_name = 'program.html'

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event-detail.html'

    def get_context_data(self, *args, **kwargs):
        event = self.get_object()
        user = self.request.user

class RulesTemplateView(TemplateView):
    template_name = 'rules.html'

class RegistrationUpdateView(DetailView):
    model = Registration
    status = 1

    def get(self, request, *args, **kwargs):
        registration = self.get_object()
        registration.status = self.status
        registration.save()
        return redirect('registrations-list', registration.group.id)


class RegistrationPresentView(RegistrationUpdateView):
    status = 2


class RegistrationAbsentView(RegistrationUpdateView):
    status = 3
