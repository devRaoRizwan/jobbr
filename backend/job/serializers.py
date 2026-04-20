from rest_framework import serializers
from .models import Job , Application


class Job_Serializer(serializers.ModelSerializer):
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