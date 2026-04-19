from django.db import models
from accounts.models import User


# Create your models here.

class Job(models.Model):
    JOB_TYPE_CHOICES = (
        ("full_time", "Full Time"),
        ("part_time", "Part Time"),
        ("contract", "Contract"),
    )
    
    SALARY_PERIOD_CHOICES = (
        ("hour","Hourly"),
        ("month","Monthly"),
        ("year","Yearly"),
        
    )
    
    title = models.CharField(max_length= 250)
    description = models.TextField()
    employer_user = models.ForeignKey(User , on_delete= models.CASCADE)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits= 10 , decimal_places= 2)
    salary_period = models.CharField(max_length= 12 , choices= SALARY_PERIOD_CHOICES , default= 'month')
    currency = models.CharField(max_length=3)
    job_type = models.CharField(max_length= 12 , choices= JOB_TYPE_CHOICES , default= 'full_time')
    deadline = models.DateField(null= True , blank= True)
    is_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    
    def __str__(self):
        return self.title
