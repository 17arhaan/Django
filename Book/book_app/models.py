from django.db import models

# Create your models here.
class book_app(models.Model):
    BASE_CHOICES = [
        ('F' , 'Fiction'),
        ('N' , 'Non Fiction'),
        ('D' , 'Drama'),
        ('T' , 'Thriller'),
        ('C' , 'Comedy'),
        ('R' , 'Romance'),
    ]

    book_name = models.CharField(max_length=20)
    book_genre = models.CharField(max_length=20,choices=BASE_CHOICES)

    def __str__(self):
        return f"{self.book_name} - {self.book_genre}"
    
    class Meta:
        ordering = ['book_genre']