from django.urls import path
from .views import JobList , JobModify


urlpatterns = [
    path("" , JobList.as_view()),
    path('<int:pk>/' , JobModify.as_view() )
]