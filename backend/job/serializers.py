from rest_framework import serializers
from .models import Job


class Job_Serializer(serializers.ModelSerializer):
    class Meta :
        model = Job
        fields = "__all__"
        read_only_fields = [
            "employer_user",
            "is_closed",
            "created_at",
            "updated_at",
        ]