from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from events import views as views_events

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_events.HomeView.as_view(), name='home'),
    path('programacao', views_events.ProgramTemplateView.as_view(), name='program'),
    path('regulamento', views_events.RulesTemplateView.as_view(), name='rules'),
    path('minicurso/<int:pk>/', views_events.EventDetailView.as_view(), name='event-detail'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('change_password', views_events.change_password, name='change_password'),
    path('cadastro/', views_events.SignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]
