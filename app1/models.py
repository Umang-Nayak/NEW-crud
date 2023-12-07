from django.db import models

# Create your models here.


class Employee(models.Model):
    e_name = models.CharField(max_length=100)
    e_post = models.CharField(max_length=100)
    e_contact = models.CharField(max_length=15)
    e_email = models.EmailField()
    e_salary = models.IntegerField()
    e_address = models.CharField(max_length=500)
    e_city = models.CharField(max_length=100)

    class Meta:
        ordering = ['e_name']
        db_table = 'Employee'


