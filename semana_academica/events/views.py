from django.shortcuts import render

from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView
from events.models import Event, Registration
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from events.forms import SignUpForm
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
    template_name = 'event-detail.html'

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

class SignUpView (CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


class EventRegistrationView(DetailView):
    model = Event

    def get(self, request, *args, **kwargs):
        Registration.objects.create(event=self.get_object(), user=request.user)
        return redirect('home')