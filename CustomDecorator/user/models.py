from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self ,email , username , password = None) :
        if not email : 
            raise ValueError("Email field is required !")
        if not username : 
            raise ValueError("Username field is required !")
        if not password : 
            raise ValueError("Passowrd field is required !")
        user = self.model(
            email = email , 
            username = username 
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self , email , username , password):
        user = self.create_user(email = email , username = username , password = password)
        user.is_superuser = True
        user.is_staff = True 
        user.is_admin = True
        user.save()
        return user
    
    def create_student(self , email , username , password) : 
        user = self.create_user(email , username , password)
        user.is_student = True
        user.save()
        return user
    def create_teacher(self , email , username , password) : 
        user = self.create_user(email , username , password)
        user.is_teacher = True
        user.save()
        return user
    def create_principal(self , email , username , password) : 
        user = self.create_user(email , username , password)
        user.is_principal = True
        user.save()
        return user
        
    
class UserAccount(AbstractBaseUser):
    username    = models.CharField(max_length = 200 , blank = False , null = False)
    email       = models.CharField(max_length = 200 , blank = False , null = False , unique = True)
    
    is_active       = models.BooleanField(default = True)
    is_staff        = models.BooleanField(default = False)
    is_admin        = models.BooleanField(default = False)
    is_superuser    = models.BooleanField(default = False)
    
    is_student      = models.BooleanField(default = False)
    is_teacher      = models.BooleanField(default = False)
    is_principal    = models.BooleanField(default = False)
    
    objects         = UserAccountManager()
    
    USERNAME_FIELD  = "email"
    
    def __unicode__(self):
        return str(self.username)
    
    def has_perm(self , perm , obj = None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    