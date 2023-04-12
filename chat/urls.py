from django.urls import path

from .views import ThreadView, ListOwnerThread

urlpatterns = [
    path('thread/', ThreadView.as_view(), name='thread'),
    path('thread/<int:pk>/', ThreadView.as_view(), name='thread_detail'),
    path('thread/list/owner/<int:pk>', ListOwnerThread.as_view(), name='thread_detail'),
]
