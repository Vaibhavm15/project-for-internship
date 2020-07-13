from django.db import models
from django.contrib.postgres.fields import ArrayField
from postgres_copy import CopyManager

class Order(models.Model):
    Id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    order_name = models.CharField(max_length = 100)
    user_id = models.ForeignKey('Customer' , on_delete=models.CASCADE)
    amount = models.FloatField()
    objects = CopyManager()




class Customer(models.Model):
    user_id = models.CharField(max_length = 100,primary_key=True )
    login =  models.CharField(max_length = 100 )
    password = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    company_id = models.OneToOneField("Company" , on_delete=models.CASCADE)
    credit_cards = ArrayField(models.CharField(max_length = 100) , blank = True)
    objects = CopyManager()

class Company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length = 100 )
    objects = CopyManager()
