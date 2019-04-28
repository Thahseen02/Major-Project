from django.db import models

# Create your models here.

class Input(models.Model):
    Grade_Choices = (
        ('S', 'S'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )
    Gender_Choices = (
        ('F','Female'),
        ('M','Male'),
        ('O','other'),
    )
    Internship_Choices = (
        ('Y','Yes'),
        ('N','No'),
    )
    user_name = models.CharField(max_length=25,verbose_name='Name')
    roll_number= models.CharField(max_length=25,verbose_name='Roll Number')
    gender = models.CharField(max_length=1, choices=Gender_Choices,verbose_name='Gender')
    cgpa = models.FloatField(verbose_name='CGPA')
    school_grade = models.FloatField(verbose_name='12th Grade')
    internship = models.CharField(max_length=1,choices=Internship_Choices,verbose_name='Internship Experience')
    os = models.CharField(max_length=1,choices=Grade_Choices,verbose_name='Grade in Operating Sytems')
    networks = models.CharField(max_length=1,choices=Grade_Choices,verbose_name='Grade in Networks')
    dbms = models.CharField(max_length=1,choices=Grade_Choices,verbose_name='Grade in DBMS ')
    dsa = models.CharField(max_length=1,choices=Grade_Choices,verbose_name='Grade in DSA')
#    interviews = models.FloatField(verbose_name='Number Of Interviews Attended')
    
    
    
    
    
