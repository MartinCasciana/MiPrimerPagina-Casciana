from django.urls import path
from django.http import HttpResponse

def about_view(request):
    return HttpResponse("Acerca de mí (placeholder)")

urlpatterns = [
    path('', about_view, name='about'),
]
