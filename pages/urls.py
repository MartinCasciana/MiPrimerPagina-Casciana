from django.urls import path
from django.http import HttpResponse

def placeholder_list(request):
    return HttpResponse("Pages: listado (placeholder)")

urlpatterns = [
    path('', placeholder_list, name='page_list'),
]
