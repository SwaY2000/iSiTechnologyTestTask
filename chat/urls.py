from django.urls import path

from .views import ThreadView

urlpatterns = [
    path('thread/', ThreadView.as_view(), name='thread'),
]
