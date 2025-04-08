from django.db import models
from . mod
# Create your models here.
class Prisoner(models.Model):
    BLOCK_CHOICES =[
        ('A','Block A'),
        ('B','Block B'),
        ('C','Block C'),
        ('D','Block D'),
    ]
    prisoner_id = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length = 20 , unique = True)
    age = models.IntegerField()
    block_number = models.CharField(max_length=1, choices=BLOCK_CHOICES)
    cell_number = models.IntegerField()
    admission_date = models.DateField()
    release_date = models.DateField(null=True, blank=True)
    crime = models.TextField()
    
    def __str__(self):
        return f"{self.prisoner_id} - {self.name}"

    class Meta:
        ordering = ['block_number', 'cell_number']