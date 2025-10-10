from django.urls import path
from django.http import HttpResponse

def login_placeholder(request):
    return HttpResponse("Login (placeholder)")

urlpatterns = [
    path('login/', login_placeholder, name='login'),
]
