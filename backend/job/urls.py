from django.urls import path
from .views import JobList , JobModify , ApplyList , UpdateApplicationStatus


urlpatterns = [
    path("" , JobList.as_view()),
    path('<int:pk>/' , JobModify.as_view() ),
    path('<int:pk>/apply/' ,ApplyList.as_view() ),
    path('applications/<int:application_pk>/', UpdateApplicationStatus.as_view()),
 
]