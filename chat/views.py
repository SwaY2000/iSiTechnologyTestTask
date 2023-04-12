from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Thread, Message
from .paginations import CustomThreadOwnerList
from .serializers import ThreadSerializer, MessageSerializer


class ThreadView(APIView):
    def post(self, request):
        serializer = ThreadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=serializer.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        thread = get_object_or_404(Thread, pk=pk)
        thread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListOwnerThread(ListAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    pagination_class = CustomThreadOwnerList

    def get_queryset(self):
        return Thread.objects.filter(participants__id=self.kwargs.get('pk', ' '))


class MessageView(APIView):
    def post(self, request, pk):
        request.data.update({'sender': 1,
                             'thread': pk})
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageInThreadListView(ListAPIView):
    serializer_class = MessageSerializer
    queryset = Thread.objects.all()
    pagination_class = CustomThreadOwnerList

    def get_queryset(self):
        threads = get_object_or_404(Thread, id=self.kwargs.get('pk', ' '),
                                    participants=get_object_or_404(get_user_model(), id=1))
        return Message.objects.filter(thread=threads)
