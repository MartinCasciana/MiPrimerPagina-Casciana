from django.urls import path
from .views import inbox_list, sent_list, message_detail, compose, delete_message

urlpatterns = [
    path('', inbox_list, name='inbox_home'),
    path('sent/', sent_list, name='inbox_sent'),
    path('new/', compose, name='inbox_new'),
    path('to/<str:username>/', compose, name='inbox_new_to'),
    path('<int:pk>/', message_detail, name='inbox_detail'),
    path('<int:pk>/delete/', delete_message, name='inbox_delete'),
]
