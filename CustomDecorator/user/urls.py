from django.urls import path
from user import views as user_views
from django.contrib.auth.views import LoginView

app_name = "user_urls"

urlpatterns = [
    path("" , user_views.homePage , name = "home-page") , 
    path("login-user/" , LoginView.as_view(template_name = "user/loginView.html") , name = "login-user") , 
    path("student-view/" , user_views.studentView , name = "student-view") , 
    path("teacher-view/" , user_views.teacherView , name = "teacher-view") , 
    path("principal-view/" , user_views.principalView , name = "principal-view") , 
]