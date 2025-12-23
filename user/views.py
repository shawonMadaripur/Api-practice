from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializer import UserProfileSerializer

# Create your views here.

class UserProfileListCreate(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('successfully created')
        return Response(serializer.errors, status=400)