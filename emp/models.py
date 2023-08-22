from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    salary = models.DecimalField(null=True, max_digits=9, decimal_places=2)
    age = models.IntegerField(blank=True,null=True)
    email = models.EmailField(max_length=70)

    def __str__(self):
        return self.first_name
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name