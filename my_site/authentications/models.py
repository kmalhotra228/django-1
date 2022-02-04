from django.db import models

# Create your models here.
class Joinee(models.Model):
    username = models.CharField(max_length = 30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    Gender_choices = (
        ("M","Male"),
        ("F","Female")
    )
    gender = models.CharField(max_length=1,choices=Gender_choices)
    password = models.CharField(max_length=50)

class Personal_details(models.Model):
    username = models.CharField(max_length = 30 ,unique = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name = "email",max_length=100)
    phone_number = models.CharField(max_length = 10)
    date_of_birth = models.DateField()
    Gender_choices = (
        ("M","Male"),
        ("F","Female")
    )
    gender = models.CharField(max_length=1,choices=Gender_choices)

    def __str__(self):
        return f'{self.username} {self.first_name} {self.last_name} {self.gender}'

