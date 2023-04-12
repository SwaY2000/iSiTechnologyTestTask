from django.urls import path

from .views import ThreadView, ListOwnerThread, MessageView, MessageInThreadListView

urlpatterns = [
    path('thread', ThreadView.as_view(), name='thread'),
    path('thread/<int:pk>', ThreadView.as_view(), name='thread_detail'),
    path('thread/all/owner/<int:pk>', ListOwnerThread.as_view(), name='thread_list_owner'),
    path('thread/<int:pk>/messages', MessageView.as_view(), name='thread_detail'),
    path('thread/<int:pk>/messages/all', MessageInThreadListView.as_view(), name='thread_list_message'),
]
