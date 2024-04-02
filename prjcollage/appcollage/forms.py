from django import forms
from .models import *
from django.contrib.auth.hashers import make_password


        

class Course_fm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets={
            'course_name': forms.TextInput(attrs={'class': 'form-control ' ,}),
            'donation': forms.NumberInput(attrs={'class': 'form-control'}),
            'number_of_years': forms.NumberInput(attrs={'class': 'form-control'}),
            'fee_per_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'sem_wise_fee': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_fee': forms.NumberInput(attrs={'class': 'form-control',}),
           
         }       
        



class Affiliation_fm(forms.ModelForm):
    class Meta:
        model = Affiliation
        fields = '__all__'
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
         }       
        



class Country_fm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        widgets={
           'country': forms.TextInput(attrs={'class': 'form-control'}),
         }    




class University_fm(forms.ModelForm):
    class Meta:
        model = University
        fields = '__all__'
        widgets={
             'university': forms.TextInput(attrs={'class': 'form-control'}),
           
         }    




class Branch_Management_fm(forms.ModelForm):
    class Meta:
        model = Branch_Management
        fields = '__all__'
        widgets={
           'branch_management': forms.TextInput(attrs={'class': 'form-control'}),
         }       
        



class Employee_role_fm(forms.ModelForm):
    class Meta:
        model = Employee_role
        fields = '__all__'
        widgets={
            'employee_role': forms.TextInput(attrs={'class': 'form-control'}),
           
         }     



class List_College_fm(forms.ModelForm):
    class Meta:
        model = List_College
        fields = '__all__'
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'affiliation': forms.Select(attrs={'class': 'form-control'}),
            'courses': forms.Select(attrs={'class': 'form-control', 'rows': 3}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'university': forms.Select(attrs={'class': 'form-control'}),

           
         }                       





class Student_Management_fm(forms.ModelForm):
    class Meta:
        model = Student_Management
        fields = '__all__'
        widgets={
             'name_of_student': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'course_name': forms.Select(attrs={'class': 'form-control'}),
            'college_name': forms.Select(attrs={'class': 'form-control'}),
            'payment': forms.NumberInput(attrs={'class': 'form-control'}),
           
         }               
        



class Create_Employee_fm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
    
    class Meta:
        model = User
        fields = ['name', 'email', 'branch', 'phone_number', 'employee_role', 'target_per_month', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),  # Assuming branch is a ForeignKey field
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'employee_role': forms.Select(attrs={'class': 'form-control'}),  # Assuming employee_role is a ForeignKey field
            'target_per_month': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    def save(self, commit=True):
        user = super(Create_Employee_fm, self).save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user
