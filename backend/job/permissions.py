from rest_framework.permissions import BasePermission

class IsEmployer(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'employer'
    

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.employer_user == request.user
    
    
class IsJobseeker(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'jobseeker'