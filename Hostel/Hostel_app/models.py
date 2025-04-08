from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    roll_no = models.IntegerField()
    hostel = models.CharField(max_length=50)
    room_no = models.CharField(max_length=10)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.hostel}"
