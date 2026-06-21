from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to SkillSync")

def dashboard(request):
    return HttpResponse("Welcome to SkillSync Dashboard")

urlpatterns = [
    path('', include('accounts.urls')),
    path("dashboard/", dashboard),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]