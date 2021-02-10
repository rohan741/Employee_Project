from django.db import models

# model defines the table that will be created in database with defined data type
# Django follows ORM (object relational mapper) to create database with the fields defined in model
# In database, Employee table is created that will contain employee data 
class Employee(models.Model):
    email= models.EmailField()
    name= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    password= models.CharField(max_length=50)
    Employee_id= models.CharField(max_length=10)
    address= models.TextField() 
    dob= models.DateField()
    company= models.CharField(max_length=50)
    mobile= models.CharField(max_length=10)
    city=models.CharField(max_length=20)
    def __str__(self):
        return self.name