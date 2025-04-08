from django.db import models

# Create your models here.
class Classroom_app(models.Model):
    BLOCK_CHOICES = [
        ('A',"Grade I"),
        ('B',"Grade II"),
        ('C',"Grade III"),
        ('D',"Grade IV"),
        ('E',"Grade V"),
    ]
    student_name = models.CharField(max_length = 20)
    student_grade = models.CharField(max_length = 10,choices = BLOCK_CHOICES)
    student_section = models.CharField(max_length = 1)
    teacher_name = models.CharField(max_length = 20)
    total_marks = models.IntegerField()
    admission_date = models.DateField()
    student_disablity = models.TextField()

    def __str__(self):
        return f"{self.teacher_name} - {self.student_name}"
    
class Meta():
    ordering = ['total_marks']