from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length= 30)
    phone = models.CharField(max_length= 12)
    problem = models.TextField()
    
    #ekahane self.name return korar karon holo jate submit korar pr name dekhai 
    def __str__(self):
        return self.name 
    #admin e contact uss hoye geche tai etar jono :
    class Meta:
        verbose_name_plural= "Contact Us"