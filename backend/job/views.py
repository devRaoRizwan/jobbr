from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated , AllowAny
from .models import Job
from .serializers import Job_Serializer

# Create your views here.


class JobList(ListCreateAPIView):
    queryset = Job.objects.filter(is_closed = False)
    serializer_class = Job_Serializer
    
    def get_permissions(self):
        if self.request.method == "GET":
            return[AllowAny()]
        return [IsAuthenticated()]
            
    
    def perform_create(self, serializer):
        serializer.save(employer_user = self.request.user)
    
    
class JobModify(RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = Job_Serializer
    lookup_field = "pk"