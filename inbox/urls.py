from django.urls import path
from django.http import HttpResponse

def inbox_placeholder(request):
    return HttpResponse("Inbox (placeholder)")

urlpatterns = [
    path('', inbox_placeholder, name='inbox_home'),
]
