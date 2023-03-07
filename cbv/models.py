from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField()
    class Meta:
        db_table = 'food'
    def __str__(self):
        return self.name