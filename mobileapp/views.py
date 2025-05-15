from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import JobApplication
from .serializers import JobApplicationSerializer
from django.shortcuts import get_object_or_404


class JobApplicationListCreateAPIView(APIView):
    """
    API view to list all job applications (authenticated) or create a new one (unauthenticated).
    """

    def get_permissions(self):
        # Allow unauthenticated POST, require authentication for GET
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        applications = JobApplication.objects.all()
        serializer = JobApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobApplicationRetrieveUpdateDestroyAPIView(APIView):
    """
    API view to retrieve, update, or delete a specific job application (authenticated).
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(JobApplication, pk=pk)

    def get(self, request, pk):
        application = self.get_object(pk)
        serializer = JobApplicationSerializer(application)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        application = self.get_object(pk)
        serializer = JobApplicationSerializer(application, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        application = self.get_object(pk)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
