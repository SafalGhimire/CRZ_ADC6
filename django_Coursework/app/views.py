from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import Template,Context 
from django.views.generic import TemplateView, ListView, CreateView
from .models import Student
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .forms import BookForm
from .models import Book

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


def search(request):
    if request.method=='POST':
        srch = request.POST['search']

        if srch:
            match = Student.objects.filter(
                Q(first_Name__icontains=srch) | Q(Address__icontains=srch)
                )

            if match:
                return render(request,'students/search.html', {'sr':match})
            else:
                messages.error(request,'result not found')
        else:
            return HttpResponseRedirect('/search/')

    return render(request,'search.html')


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })


def delete_book(request, ID):
    if request.method == 'POST':
        book = Book.objects.get(id=ID)
        book.delete()
    return redirect('book_list')


class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'

def view_register_user(request):
    if request.method =="GET":
        return render(request,'auth/register.html')
    else:
        print(request.POST)
        user = User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        user.save()
        return HttpResponse("Signup Successful")


def view_authenticate_user(request):
    if request.method =="GET":
        return render (request,'auth/login.html')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['input_username'],password=request.POST['input_password'])
        print(user)
        if user is not None:
            login(request,user)
            return render(request,'students/student.html')
        else:
            return HttpResponse('Authentication Failed')  

def view_logout(request):
    logout(request)
    return render(request,'students/student.html')