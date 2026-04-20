from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView , UpdateAPIView
from rest_framework.permissions import IsAuthenticated , AllowAny
from .permissions import IsEmployer , IsOwner , IsJobseeker
from .models import Job , Application
from .serializers import Job_Serializer , Application_Serializer , ApplicationStatusSerializer
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError


# Create your views here.


class JobList(ListCreateAPIView):
    queryset = Job.objects.filter(is_closed = False)
    serializer_class = Job_Serializer
    
    def get_permissions(self):
        if self.request.method == "GET":
            return[AllowAny()]
        
        if self.request.method == "POST":
            return[IsEmployer()]
        return [IsAuthenticated()]

            
    
    def perform_create(self, serializer):
        serializer.save(employer_user = self.request.user)
    
    
class JobModify(RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = Job_Serializer
    lookup_field = "pk"
    
    def get_permissions(self):
        if self.request.method == "GET" :
            return[AllowAny()]
        return[IsOwner()]
    
    
class ApplyList(ListCreateAPIView):
    serializer_class = Application_Serializer
    
    def get_queryset(self):
        job = get_object_or_404(Job , pk = self.kwargs['pk'])
        if self.request.method == 'GET' :
            if job.employer_user != self.request.user :
                raise ValidationError({"detail": "You are not the owner of this job."})
        return Application.objects.filter(job = job)
            
    def get_permissions(self):
        if self.request.method == "POST":
            return[IsJobseeker()]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        job = get_object_or_404(Job , pk = self.kwargs['pk'])
        if Application.objects.filter(job=job, applicant=self.request.user).exists():
            raise ValidationError({"detail": "You have already applied to this job."})
        serializer.save(applicant=self.request.user, job=job)
        

class UpdateApplicationStatus(UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationStatusSerializer
    lookup_field = "application_pk"
    
    def get_permissions(self):
        return [IsAuthenticated()]
    
    def get_object(self):
        application = get_object_or_404(Application , pk = self.kwargs['application_pk'])
        if application.job.employer_user != self.request.user :
            raise ValidationError({"detail": "You are not the owner of this job."})
        return application
        
            
        