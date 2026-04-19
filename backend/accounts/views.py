from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import User_Serializer
from .models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(["POST"])
def register(request):
    serializer = User_Serializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = User_Serializer(request.user)
    return Response(serializer.data , status= status.HTTP_200_OK)
    