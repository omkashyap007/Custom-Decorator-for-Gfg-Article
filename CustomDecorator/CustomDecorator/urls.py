from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , include("user.urls" , namespace = "user_urls")) , 
]


"""

from user.models import UserAccount

student = UserAccount.objects.create_student(username = "student" , email = "studentmail@gmail.com" , password = "testing123")

student = UserAccount.objects.create_teacher(username = "teacher" , email = "teachermail@gmail.com" , password = "testing123")

principal = UserAccount.objects.create_principal(username = "principal" , email = "principalmail@gmail.com" , password = "testing123")


"""