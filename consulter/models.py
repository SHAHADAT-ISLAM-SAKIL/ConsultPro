from django.db import models
from django.contrib.auth.models import User
from client.models import Client
# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length= 30)
    slug = models.SlugField(max_length= 40)
    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length= 30)
    slug = models.SlugField(max_length= 40)
    def __str__(self):
        return self.name

class AvailableTime(models.Model):
    name = models.CharField(max_length= 100)
    def __str__(self):
        return self.name

class Consulter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="consulter/images/", default='consulter/images/default.jpg')
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Specialization)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

STAR_CHOICES = [
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
   
class Review(models.Model):
    reviewer = models.ForeignKey(Client, on_delete= models.CASCADE)
    consulter = models.ForeignKey(Consulter, on_delete= models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add= True)
    rating = models.CharField(choices= STAR_CHOICES, max_length= 10)
    
    def __str__(self):
        return f"Clint : {self.reviewer.user.first_name} ; Consulter : {self.consulter.user.last_name}"
    