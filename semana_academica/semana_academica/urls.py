from django.contrib import admin
from django.urls import path
from events import views as views_events

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_events.HomeView.as_view(), name='home'),
    path('programacao', views_events.ProgramTemplateView.as_view(), name='program'),
    path('regulamento', views_events.RulesTemplateView.as_view(), name='rules'),
    path('minicurso/<int:pk>/', views_events.EventDetailView.as_view(), name='event-detail'),
]
