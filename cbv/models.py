from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    class Meta:
        db_table = 'food'
    def __str__(self):
        return self.name
    
class AddFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='upload/')
    
    class Meta:
        db_table ='addfile'
    
    