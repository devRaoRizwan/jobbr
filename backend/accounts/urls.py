from django.urls import path
from .views import register , current_user
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

urlpatterns = [
    path("register/" , register ),
    path("me/" , current_user),
    
    # jwt urls
    path("login/" , TokenObtainPairView.as_view() , name="token_obtain_pair"),
    path("token/refresh/" , TokenRefreshView.as_view() , name="token_refresh"),
]