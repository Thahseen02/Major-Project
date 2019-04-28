from django.db import models

class Question(models.Model):
    question_choices=(
        ('E','Easy'),
        ('M','Medium'),
        ('H','Hard')
    )
    subject_choices=(
        ('OS','OS'),
        ('DBMS','DBMS'),
        ('DSA','DSA'),
        ('NET','NETWORKS')
    )
    question = models.CharField(max_length=10000)
    category = models.CharField(max_length=1,choices=question_choices)
    subject = models.CharField(max_length=7,choices=subject_choices)
    a_choice = models.CharField(max_length=10000)
    b_choice = models.CharField(max_length=10000)
    c_choice = models.CharField(max_length=10000)
    d_choice = models.CharField(max_length=10000)
    correct = models.CharField(max_length=10000)
    
    def __str__(self):
        return '%s %s' % (self.subject, self.category)

    
#Category for adaptive set of questions    
#E->D : 1 
#D->C : 2
#C->B : 3
#B->A : 4
#A->S : 5    

class Adaptive_Question(models.Model):
    question_choices=(
        ('1','E->D'),
        ('2','D->C'),
        ('3','C->B'),
        ('4','B->A'),
        ('5','A->S')
    )
    subject_choices=(
        ('OS','OS'),
        ('DBMS','DBMS'),
        ('DSA','DSA'),
        ('NET','NETWORKS')
    )
    question = models.CharField(max_length=10000)
    category = models.CharField(max_length=1,choices=question_choices)
    subject = models.CharField(max_length=7,choices=subject_choices)
    a_choice = models.CharField(max_length=10000)
    b_choice = models.CharField(max_length=10000)
    c_choice = models.CharField(max_length=10000)
    d_choice = models.CharField(max_length=10000)
    correct = models.CharField(max_length=10000)
    
    def __str__(self):
        return '%s %s' % (self.subject, self.category)

    
