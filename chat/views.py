from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ThreadSerializer


class ThreadView(APIView):
    def post(self, request):
        serializer = ThreadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=serializer.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
