from django.db import models

# Create your models here.
class Contact_us(models.Model):
    name = models.CharField(max_length=200,null=False)
    email = models.EmailField(max_length=254,null=False,blank=False)
    phone_number = models.CharField(max_length=15, help_text="+255 format",null=False,blank=False)
    subject = models.CharField(max_length=100,null=False,blank=False)
    message = models.TextField(null=False,blank=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
