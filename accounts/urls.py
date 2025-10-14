from django.urls import path
from .views import (
    signup_view, login_view, logout_view,
    profile_view, profile_edit_view, password_change_view
)

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('password/change/', password_change_view, name='password_change'),
]

