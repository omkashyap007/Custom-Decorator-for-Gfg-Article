from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse

def student_test_function(user) :
    if user.is_student : 
        return True
    return False
def teacher_test_function(user) :
    if user.is_teacher : 
        return True
    return False
def principal_test_function(user) :
    if user.is_principal : 
        return True
    return False

def student_access_only():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request , *args , **kwargs):
            if not student_test_function(request.user):
                return HttpResponse("You are not a student and you are not allowed to access this page !") 
            return view(request , *args , **kwargs)
        return _wrapped_view
    return decorator
def teacher_access_only(view_to_return = "user_urls:home-page"):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request , *args , **kwargs):
            if not teacher_test_function(request.user):
                messages.error(request , "You cannot access the teachers  page !")
                return redirect(view_to_return)
            return view(request , *args , **kwargs)
        return _wrapped_view
    return decorator

def principal_access_only(message_to_deliver = "Not allowed to access the principal's page , login as principal !"):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request , *args , **kwargs):
            if not principal_test_function(request.user):
                messages.error(request , message_to_deliver)
                return redirect("user_urls:login-user")
            return view(request , *args , **kwargs)
        return _wrapped_view
    return decorator



"""

def test_function_works(*args , **kwargs):
  	if args[0] == True : 
      return True
    return False

def some_decorator(*decorator_args , **decorator_kwargs):
    def decorator(view_function):
        @wraps(view_function)
        def _wrapped_view(request, *view_args, **view_kwargs):
            print("The required actions will be taken here ! Well ,actually inside the _wrapped_view function")
            if not test_function_works(request.user):
                print("The necessary operation that will be taken if the test case fails !")
            return view_function(request, *args, **kwargs)
        return _wrapped_view
    return decorator

urls : 
    studnent-view 
    teacher-view 
    principal-view 
    
    
    home-page   : links to all the views in the page .
                : does not have any decorator so that it can be accessed by all the users. 
                : will have messages to get access to the errors or success sent by the view.
                
    login-view  : this view is for logging in . 
                : this page does not have any decorators so that this can be accessed . 
                : will have messages to get access to the errors or success sent by the view.


Code explanation  :

principal_access_only is the name of the function/decorator which will be wrapped around the view , it may take arguments as per the requirement , 

like principal_access_only takes the message_to_deliver argument , you can create your own variable and take care of the way you want the decorator to work . 

then we create the function decorator which takes the view on which the decorator will be wrapped . 

the funtool function wraps() takes the view on which the decorator will be wrapped . 

then the _wrapped_view() acts the same , well its the same view because of the arguments passed . Now you can treat this as a particular view and can make conditions which need to be fulfilled before the view actually loads up . 

Hence , we created a decorator . 



"""