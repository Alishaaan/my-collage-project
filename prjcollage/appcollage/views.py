from django.shortcuts import render,redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.




def page(request):
    return render(request,"dash.html")



def cresult(request):
    course=Course.objects.all()
    return render(request,"course.html",{'stu':course})



def cforms(request):
    if request.method == 'POST':
        fm = Course_fm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Course_fm()
            return redirect('cresult')
     
    else:
        fm = Course_fm()
    stu=Course.objects.all()
    return render (request,'coursefm.html',{'fm':fm,'stu':stu})
   
#edit

def edit_course(request, pk):
 task = Course.objects.get(pk=pk)
 if request.method == 'POST':
     form = Course_fm(request.POST, instance=task)
     if form.is_valid():
         form.save()
         return redirect('cresult')
 else:
     form = Course_fm(instance=task)
 return render(request, 'Cedit.html', {'form': form, 'task': task})


#delete


def delete_course(request, pk):
    task = Course.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('cresult')
    return render(request, 'Cdelete.html', {'task': task})

#def delete_course(request, pk):
#    task = Course.objects.get(pk=pk)
#    task.delete()
#    return redirect('result')
#

#affiliation
#def aresult(request):
#    course=Affiliation.objects.all()
#    return render(request,"affiliation.html",{'stu':course})
#



def aresult(request):
    affiliations = Affiliation.objects.all()
    return render(request, 'affiliation.html', {'affiliations': affiliations})

def aforms(request):
    if request.method == 'POST':
        fm = Affiliation_fm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('aresult')
    else:
        fm = Affiliation_fm()
    return render(request, 'affiliationfm.html', {'fm': fm})

def edit_affiliation(request, pk):
    task = get_object_or_404(Affiliation, pk=pk)
    if request.method == 'POST':
        form = Affiliation_fm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('aresult')
    else:
        form = Affiliation_fm(instance=task)
    return render(request, 'Aedit.html', {'form': form})

def delete_affiliation(request, pk):
    affiliation = get_object_or_404(Affiliation, pk=pk)
    if request.method == 'POST':
        affiliation.delete()
        return redirect('aresult')
    return render(request, 'Adelete.html', {'affiliation': affiliation})






#def aresult(request):
#    course = Affiliation.objects.all()
#    return render(request, 'affiliation.html', {'stu': course})
#
#def aforms(request):
#    if request.method == 'POST':
#        fm = Affiliation_fm(request.POST, request.FILES)
#        if fm.is_valid():
#            fm.save()
#            return redirect('aresult')
#    else:
#        fm = Affiliation_fm()
#    return render(request, 'affiliationfm.html', {'fm': fm})
#


#def aforms(request):
#    if request.method == 'POST':
#        fm = Affiliation_fm(request.POST,request.FILES)
#        if fm.is_valid():
#            fm.save()
#            fm=Affiliation_fm()
#            return redirect('aresult')
#     
#    else:
#        fm = Affiliation_fm()
#    stu=Affiliation.objects.all()
#    return render (request,'affiliationfm.html',{'fm':fm,'stu':stu})
#


#edit


#def edit_affiliation(request, pk):
#    task = get_object_or_404(Affiliation, pk=pk)
#    if request.method == 'POST':
#        form = Affiliation_fm(request.POST, request.FILES, instance=task)
#        if form.is_valid():
#            form.save()
#            return redirect('aresult')
#    else:
#        form = Affiliation_fm(instance=task)
#    return render(request, 'Aedit.html', {'form': form})
#
#

#def edit_affiliation(request, pk):
# task = Affiliation.objects.get(pk=pk)
# if request.method == 'POST':
#     form = Affiliation_fm(request.POST,request.FILES, instance=task)
#     if form.is_valid():
#         form.save()
#         return redirect('aresult')
# else:
#     form = Affiliation_fm(instance=task)
# return render(request, 'Aedit.html', {'form': form, 'task': task})
#

#delete


#def delete_affiliation(request, pk):
#    task = get_object_or_404(Affiliation, pk=pk)
#    if request.method == 'POST':
#        task.delete()
#        return redirect('aresult')
#    return render(request, 'Adelete.html', {'task': task})
#








#def delete_affiliation(request, pk):
#    task = Affiliation.objects.get(pk=pk)
#    if request.method == 'POST':
#        task.delete()
#        return redirect('aresult')
#    return render(request, 'Adelete.html', {'task': task})
#


#country


def cyresult(request):
    course=Country.objects.all()
    return render(request,"country.html",{'stu':course})




def cyforms(request):
    if request.method == 'POST':
        fm = Country_fm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Country_fm()
            return redirect('cyresult')
     
    else:
        fm = Country_fm()
    stu=Country.objects.all()
    return render (request,'countryfm.html',{'fm':fm,'stu':stu})
   


#edit

def edit_country(request, pk):
 task = Country.objects.get(pk=pk)
 if request.method == 'POST':
     form = Country_fm(request.POST, instance=task)
     if form.is_valid():
         form.save()
         return redirect('cyresult')
 else:
     form = Country_fm(instance=task)
 return render(request, 'CYedit.html', {'form': form, 'task': task})


#delete

def delete_country(request, pk):
    task = Country.objects.get(pk=pk)
    task.delete()
    return redirect('cyresult')








#university


def uresult(request):
    course=University.objects.all()
    return render(request,"university.html",{'stu':course})




def uforms(request):
    if request.method == 'POST':
        fm = University_fm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=University_fm()
            return redirect('uresult')
     
    else:
        fm = University_fm()
    stu=University.objects.all()
    return render (request,'universityfm.html',{'fm':fm,'stu':stu})
   


#edit

def edit_university(request, pk):
 task = University.objects.get(pk=pk)
 if request.method == 'POST':
     form = University_fm(request.POST, instance=task)
     if form.is_valid():
         form.save()
         return redirect('uresult')
 else:
     form = University_fm(instance=task)
 return render(request, 'Uedit.html', {'form': form, 'task': task})


#delete

def delete_university(request, pk):
    task = University.objects.get(pk=pk)
    task.delete()
    return redirect('uresult')






#branch


def bresult(request):
    course=Branch_Management.objects.all()
    return render(request,"branch.html",{'stu':course})




def bforms(request):
    if request.method == 'POST':
        fm = Branch_Management_fm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Branch_Management_fm()
            return redirect('bresult')
     
    else:
        fm = Branch_Management_fm()
    stu=Branch_Management.objects.all()
    return render (request,'branchfm.html',{'fm':fm,'stu':stu})
   


#edit

def edit_branch(request, pk):
 task = Branch_Management.objects.get(pk=pk)
 if request.method == 'POST':
     form = Branch_Management_fm(request.POST, instance=task)
     if form.is_valid():
         form.save()
         return redirect('bresult')
 else:
     form = Branch_Management_fm(instance=task)
 return render(request, 'bedit.html', {'form': form, 'task': task})


#delete

def delete_branch(request, pk):
    task = Branch_Management.objects.get(pk=pk)
    task.delete()
    return redirect('bresult')







#employee


def eresult(request):
    course=Employee_role.objects.all()
    return render(request,"employee.html",{'stu':course})




def eforms(request):
    if request.method == 'POST':
        fm = Employee_role_fm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Employee_role_fm()
            return redirect('eresult')
     
    else:
        fm = Employee_role_fm()
    stu=Employee_role.objects.all()
    return render (request,'employeefm.html',{'fm':fm,'stu':stu})
   


#edit

def edit_employee(request, pk):
 task = Employee_role.objects.get(pk=pk)
 if request.method == 'POST':
     form = Employee_role_fm(request.POST, instance=task)
     if form.is_valid():
         form.save()
         return redirect('eresult')
 else:
     form = Employee_role_fm(instance=task)
 return render(request, 'Eedit.html', {'form': form, 'task': task})


#delete

def delete_employee(request, pk):
    task = Employee_role.objects.get(pk=pk)
    task.delete()
    return redirect('eresult')





#list of collage


def lresult(request):
    course=List_College.objects.all()
    return render(request,"list.html",{'stu':course})




def lforms(request):
    if request.method == 'POST':
        fm = List_College_fm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=List_College_fm()
            return redirect('lresult')
     
    else:
        fm = List_College_fm()
    stu=List_College.objects.all()
    return render (request,'listfm.html',{'fm':fm,'stu':stu})
   


#edit

def edit_list(request, pk):
 task = List_College.objects.get(pk=pk)
 if request.method == 'POST':
     form = List_College_fm(request.POST, instance=task)
     if form.is_valid():
         form.save()
         return redirect('lresult')
 else:
     form = List_College_fm(instance=task)
 return render(request, 'Ledit.html', {'form': form, 'task': task})


#delete

def delete_list(request, pk):
    task = List_College.objects.get(pk=pk)
    task.delete()
    return redirect('lresult')



#studentof management


def sresult(request):
    course=Student_Management.objects.all()
    return render(request,"student.html",{'stu':course})




def sforms(request):
    if request.method == 'POST':
        fm = Student_Management_fm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Student_Management_fm()
            return redirect('sresult')
     
    else:
        fm = Student_Management_fm()
    stu=Student_Management.objects.all()
    return render (request,'studentfm.html',{'fm':fm,'stu':stu})
   


#edit

def edit_student(request, pk):
 task = Student_Management.objects.get(pk=pk)
 if request.method == 'POST':
     form = Student_Management_fm(request.POST, instance=task)
     if form.is_valid():
         form.save()
         return redirect('sresult')
 else:
     form = Student_Management_fm(instance=task)
 return render(request, 'Sedit.html', {'form': form, 'task': task})


#delete

def delete_student(request, pk):
    task = Student_Management.objects.get(pk=pk)
    task.delete()
    return redirect('sresult')



def home(request):
    return render(request,"aaaaa.html")



def LoginPage (request):
    if request.method =='POST':
        email = request.POST['email']
        print(email)
        password =request.POST['password']
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            print(user)
            return redirect('page')
        else:
            messages.error(request,'Invalid email or password.Please try again.')

    return render(request,'login.html',{'error':messages.get_messages(request)})


def create_employee(request):
    return render(request,"create_employee.html")



#create_employee


def ceresult(request):
    course=User.objects.all()
    return render(request,"create_employee.html",{'stu':course})




def ceforms(request):
    if request.method == 'POST':
        fm = Create_Employee_fm(request.POST)
        if fm.is_valid():
            fm.save()
            fm=Create_Employee_fm()
            return redirect('ceresult')
     
    else:
        fm = Create_Employee_fm()
    stu=User.objects.all()
    return render (request,'create_employeefm.html',{'fm':fm,'stu':stu})
   


#edit

def edit_create_employee(request, pk):
 task = User.objects.get(pk=pk)
 if request.method == 'POST':
     form = Create_Employee_fm(request.POST, instance=task)
     if form.is_valid():
         form.save()
         return redirect('ceresult')
 else:
     form = Create_Employee_fm(instance=task)
 return render(request, 'ceedit.html', {'form': form, 'task': task})


#delete

def delete_create_employee(request, pk):
    task = User.objects.get(pk=pk)
    task.delete()
    return redirect('ceresult')


def navbar(request):
    return render(request,"navbar.html")


def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")



def courses(request):
    course=Course.objects.all()
    return render(request,"courses.html",{'stu':course})






def collage(request):
    course=List_College.objects.all()
    return render(request,"collage.html",{'stu':course})


def gallery(request):
    return render(request,"gallery.html")

def contact(request):
    return render(request,"contact.html")