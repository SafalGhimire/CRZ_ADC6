from django.db import models


class Teacher(models.Model):
    teacher_Name = models.CharField(max_length=40)
    subject =models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.teacher_Name} teaches {self.subject}"


# Create your models here.
class Student(models.Model):
    first_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    details = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name="teacher")
    phone_No = models.IntegerField()
    address = models.CharField(max_length=50)
    student_class= models.CharField(max_length=50)


    def __str__(self):
        return f"{self.first_Name} , {self.last_Name}, {self.address} , {self.student_class}"

class Subject(models.Model):
    code =  models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return f"{self.student_Name}, {self.name} "

class Class(models.Model):
    code = models.CharField(max_length=50)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="student")

    def __str__(self):
        return f"{self.code}"

class Parents(models.Model):
    first_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    phone_No = models.IntegerField()
    address = models.CharField(max_length=50)
    student = models.OneToOneField(Student,on_delete=models.CASCADE,related_name="students")
    
    def __str__(self):
        return f"{self.first_Name} , {self.last_Name}, {self.address} " 


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


class Student_list(models.Model):
    first_Name = models.CharField(max_length=50)
    last_Name = models.CharField(max_length=50)
    phone_No = models.IntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + " " + self.first_Name + " " + self.last_Name + " " +self.address