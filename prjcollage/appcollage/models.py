from django.db import models
from django.contrib.auth.models import BaseUserManager,User,AbstractBaseUser

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=100,null=True,blank=True)
    donation = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    number_of_years = models.IntegerField(null=True,blank=True)
    fee_per_year = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    sem_wise_fee = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)

    def __str__(self):
        return f'{self.course_name}'

class Affiliation(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)  # Assuming you want to upload images to a directory named 'images/'
    def __str__(self):
        return f'{self.name}'

    
    
class Country(models.Model):   
    country = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return f'{self.country}'



class University(models.Model):   
    university = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return f'{self.university}'

class List_College(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    affiliation =  models.ForeignKey(Affiliation,on_delete=models.CASCADE,null=True,blank=True)
    courses =  models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    country=  models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    university =  models.ForeignKey(University,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f'{self.name}'







class Student_Management(models.Model):
    name_of_student = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    course_name = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    college_name =models.ForeignKey(List_College,on_delete=models.CASCADE,null=True,blank=True)
    payment = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    def __str__(self):
        return f'{self.name_of_student}'






class Branch_Management(models.Model):   
    branch_management = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return f'{self.branch_management}'
  

class Employee_role (models.Model):
    employee_role = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return f'{self.employee_role}'     


class UserManager(BaseUserManager):
    def create_user(self,name,email,password=None):
        if not email:
            raise ValueError("Users must have email")
        user = self.model(
            email= self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,name,email,password):
        user = self.create_user(
            name=name,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True 
         
        user.save(using= self._db)
        return user
    


class User(AbstractBaseUser):
    name = models.CharField(max_length=100,null=True,blank=True)  
    email = models.EmailField( verbose_name='email address',max_length=40,unique=True)
    date_joined= models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True,null=True,blank=True)
    is_staff = models.BooleanField(default=False,null=True,blank=True)
    is_admin = models.BooleanField(default=False,null=True,blank=True)
    is_superuser = models.BooleanField(default=False,null=True,blank=True)
    is_employee = models.BooleanField(default=True,null=True,blank=True)
    branch =  models.ForeignKey(Branch_Management,on_delete=models.CASCADE,null=True,blank=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    employee_role = models.ForeignKey(Employee_role,on_delete=models.CASCADE,null=True,blank=True)
    target_per_month = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
         return self.name
     
    def has_perm(self,perm,obj=None):
         return self.is_admin
     
    def has_module_perms(self,add_label):
         return True




   