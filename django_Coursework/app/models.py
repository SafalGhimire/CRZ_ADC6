from django.db import models

# Create your models here.
class Student(models.Model):
    first_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    Phoneno = models.IntegerField()
    Address = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + " " + self.first_Name + " " +self.last_Name + " " + self.Address

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)