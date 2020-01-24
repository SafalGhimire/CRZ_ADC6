from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('hello/',view_hello_world_test),
    path('test/',view_student_page),
    path('list/',view_student_lists),
    path('studentform/',view_student_form),
    path('studentform/save',view_studentdata_save),
    path('list/edit/<int:ID>',view_Studentdata_updateform),
    path('list/edit/update/<int:ID>',view_update_form_data_in_db),
    path('list/delete/<int:ID>',deletestudent),
    path('search/',search),
    path('upload/',upload),
    path('books/',book_list),
    path('books/upload/',upload_book),
    path('books/<int:pk>/',delete_book),
    path('class/books/', BookListView.as_view),
    path('class/books/upload/',UploadBookView.as_view),
    path('signup/',view_register_user),
    path('login/',view_authenticate_user), 
    path('logout/',view_logout),
    ]
