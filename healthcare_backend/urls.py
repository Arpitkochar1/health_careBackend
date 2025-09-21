from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple view for the root URL
def home_view(request):
    return HttpResponse("Welcome to the Healthcare Backend API! Use /api/auth/register/ to register a user or /admin/ for the admin interface.")

urlpatterns = [
    path('', home_view),  # Root URL handler
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]