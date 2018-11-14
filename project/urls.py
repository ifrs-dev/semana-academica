from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from events import views as views_events

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_events.HomeView.as_view(), name='home'),
    path('programacao', views_events.ProgramTemplateView.as_view(), name='program'),
    path('regulamento', views_events.RulesTemplateView.as_view(), name='rules'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('change_password', login_required(views_events.change_password), name='change_password'),
    path('cadastro/', views_events.SignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('inscricao/', login_required(views_events.RegistrationView.as_view()), name="registration"),
    path('ausente/', login_required(views_events.RegistrationPresentView.as_view()), name="registration-present"),
    path('presente/', login_required(views_events.RegistrationAbsentView.as_view()), name="registration-absent"),
]
