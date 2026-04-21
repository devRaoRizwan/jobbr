from rest_framework import serializers
from .models import Job , Application , Bookmark
from accounts.models import User 

class Employer_Serializer(serializers.ModelSerializer):
    class Meta :
        model = User 
        fields = ['id' , 'username']
        
class Job_Serializer(serializers.ModelSerializer):
    employer_user = Employer_Serializer(read_only = True)
    class Meta :
        model = Job
        fields = "__all__"
        read_only_fields = [
            "employer_user", "is_closed", "created_at","updated_at",
        ]
        
class Application_Serializer(serializers.ModelSerializer):
    class Meta :
        model = Application
        fields = "__all__"
        read_only_fields = [
            "job" , "applicant" , "status" , "submitted_at"
        ]
        
class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['status']
        
class Bookmark_Serializer(serializers.ModelSerializer):
    class Meta :
        model = Bookmark
        fields = ['job' , 'created_at']