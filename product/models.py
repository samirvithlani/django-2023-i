from django.db import models
# Create your models here.
#django orm object relational mapping

class Product(models.Model):
    #we dont have to provide id explicitly
    pName = models.CharField(max_length=100)
    pPrice = models.FloatField()
    pQty  = models.IntegerField()
    pDesc = models.CharField(max_length=100,null=True)
    pStatus = models.BooleanField(default=True)
    pColor = models.CharField(max_length=100,null=True)
    #if you dont provide table name in meta class product.product
    
    def __str__(self):
        return self.pName
        
    
    class Meta:
        db_table = 'products'
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    #emmail = varchar
    email = models.EmailField()
    password = models.CharField(max_length=100)
    salary = models.FloatField()
    age = models.PositiveIntegerField()
    joiningDate = models.DateField()
    birthDate = models.DateField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'employees'
        
        
        
    
            
    
    
