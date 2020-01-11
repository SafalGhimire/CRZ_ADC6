from django.db import models

# Create your models here.
class Student(models.Model):
    first_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    Phoneno = models.IntegerField()
    Address = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + " " + self.first_Name + " " +self.last_Name + " " + self.Address