from django.shortcuts import render
from .decorators import (
    student_access_only , 
    teacher_access_only , 
    principal_access_only   
)

def homePage(request , *args , **kwargs) : 
    context = {}
    return render(request , "user/homePage.html"  , context)

@student_access_only()
def studentView(request , *args , **kwargs):
    context = {}
    return render(request , "user/studentView.html" , context)

@teacher_access_only()
def teacherView(request , *args , **kwargs):
    context = {}
    return render(request , "user/teacherView.html" , context)

@principal_access_only()
def principalView(request , *args , **kwargs):
    context = {}
    return render(request , "user/principalView.html" , context)