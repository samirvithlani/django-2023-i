from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    fees = models.IntegerField()
    
    class Meta:
        db_table = 'course'
    
    def __str__(self):
        return self.name    

class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField() 
    
    class Meta:
        db_table = 'student' 
        
    def __str__(self):
        return self.name          

genderChoice =(("Male","male"),("Female","Female"))


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    gender = models.CharField(choices=genderChoice,max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'faculty'
    def __str__(self):
        return self.name    

class Subjects(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'subjects'
    
    def __str__(self):
        return self.name    

class Batch(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'batch'        
        
    def __str__(self):
        return self.name    
    
    
    

