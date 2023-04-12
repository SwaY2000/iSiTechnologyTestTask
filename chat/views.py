from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Thread, Message
from .paginations import CustomThreadOwnerList
from .serializers import ThreadSerializer, MessageSerializer


class ThreadView(APIView):
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    pagination_class = CustomThreadOwnerList

    def get_queryset(self):
        return Thread.objects.filter(participants__id=self.kwargs.get('pk', ' '))


class MessageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk=None):
        request.data.update({'sender': self.request.user.id,
                             'thread': pk})
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, pk_message=None):
        thread = get_object_or_404(Thread, id=pk, participants__id=self.request.user.id)
        message = get_object_or_404(Message.objects.exclude(sender__id=self.request.user.id),
                                    pk=pk_message, thread=thread)
        message.is_read = True
        message.save()
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MessageInThreadListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer
    queryset = Thread.objects.all()
    pagination_class = CustomThreadOwnerList

    def get_queryset(self):
        threads = get_object_or_404(Thread, id=self.kwargs.get('pk', ' '),
                                    participants__id=self.request.user.id)
        return Message.objects.filter(thread=threads)
