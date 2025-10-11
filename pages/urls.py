from django.urls import path
from .views import PageList, PageDetail, PageCreate, PageUpdate, PageDelete

urlpatterns = [
    path('', PageList.as_view(), name='page_list'),                 # /pages/
    path('new/create/', PageCreate.as_view(), name='page_create'),  # /pages/new/create/
    path('<slug:slug>/', PageDetail.as_view(), name='page_detail'), # /pages/<slug>/
    path('<slug:slug>/edit/', PageUpdate.as_view(), name='page_update'),
    path('<slug:slug>/delete/', PageDelete.as_view(), name='page_delete'),
]
