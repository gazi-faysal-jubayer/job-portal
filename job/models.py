from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Jobseeker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15,null=True)
    image = models.FileField()
    gender = models.CharField(max_length=10,null=True)
    type = models.CharField(max_length=15)
    def __str__(self):
        return self.user.username
    
class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15,null=True)
    image = models.FileField()
    gender = models.CharField(max_length=10,null=True)
    company = models.CharField(max_length=100,null=True)
    type = models.CharField(max_length=15)
    status = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.user.username
    
class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100)
    catagory = models.CharField(max_length=100)
    salary = models.FloatField(max_length=20)
    image = models.FileField()
    description = models.CharField(max_length=300)
    experience = models.CharField(max_length=50)
    locations = models.CharField(max_length=150)
    skills = models.CharField(max_length=100)
    creationdate = models.DateField()
    def __str__(self):
        return self.title

class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    student = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)
    resume = models.FileField(null=True)
    applydate = models.DateField()
    def __str__(self):
        return self.title
    
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=13)
    content = models.TextField()
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField(blank=True)
    def __str__(self):
        return self.title + ' by ' + self.author