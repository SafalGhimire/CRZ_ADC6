from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template,Context 

from .models import Student



def view_hello_world_test(request):
    return render(request,'students/test.html')

def view_student_lists(request):
    list_of_students= Student.objects.all()
    print(list_of_students)
    context_variable = {
        'student':list_of_students
    }
    return render(request,'students/student.html',context_variable)

def view_student_page(request):
    return render(request,'students/student.html')

def view_student_form(request):
    return render(request,'students/create.html')

def view_studentdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        get_first_Name = request.POST['first_Name']
        print(type(get_first_Name))
        get_last_Name = request.POST['last_Name']
        get_Phoneno = request.POST['Phoneno']
        get_Address = request.POST['Address']
        print(get_first_Name)
        students_obj = Student(first_Name=get_first_Name,last_Name=get_last_Name,Phoneno=get_Phoneno,Address=get_Address)
        students_obj.save()
        return HttpResponse("Record Saved")
    else:
        return HttpResponse("Error record saving")


def view_Studentdata_updateform(request,ID):
    print(ID)
    students_obj = Student.objects.get(id=ID)
    print(students_obj)
    context_varible = {
        'students': students_obj
    }
    return render(request,'students/Update.html',context_varible)

def view_update_form_data_in_db(request,ID):
    students_obj = Student.objects.get(id=ID)
    student_form_data = request.POST
    students_obj.first_Name= request.POST['first_Name']
    students_obj.last_Name =request.POST['last_Name']
    students_obj.Phoneno = request.POST['Phoneno']
    students_obj.Address = request.POST['Address']
    students_obj.save()

    return HttpResponse("Record Updated!!")

def deletestudent(request, ID):
    studentobj = Student.objects.get(id=ID)
    studentobj.delete()
    return HttpResponse("Deleted")