from django.db import models

# Create your models here.


class EmployeeDetails(models.Model):
    options=(
        ("fulltime","fulltime"),
        ("parttime","parttime"),

    )
    gender_option=(
        ("male","male"),
        ("female","female")
    )
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="images")
    email=models.EmailField()
    
    phone=models.IntegerField()
    address=models.TextField()
    Employment_type=models.CharField(max_length=50,choices=options)
    age=models.IntegerField()
    gender=models.CharField(max_length=20,choices=gender_option)
    position=models.CharField(max_length=50)
    
    
    