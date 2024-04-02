"""
URL configuration for prjcollage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appcollage import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
      path('page',views.page,name='page'),
     path('cforms',views.cforms,name='cforms'),
             path('cresult',views.cresult,name='cresult'),
             path('edit/<int:pk>/', views.edit_course, name='edit_course'),
             path('delete/<int:pk>/', views.delete_course, name='delete_course'),
             path('aforms',views.aforms,name='aforms'),
             path('aresult',views.aresult,name='aresult'),
              path('edit_affiliation/<int:pk>/', views.edit_affiliation, name='edit_affiliation'),
              path('delete_affiliation/<int:pk>/', views.delete_affiliation, name='delete_affiliation'),
               path('cyforms',views.cyforms,name='cyforms'),
               path('cyresult',views.cyresult,name='cyresult'),
               path('edit_country/<int:pk>/', views.edit_country, name='edit_country'),
                path('delete_country/<int:pk>/', views.delete_country, name='delete_country'),
                path('uforms',views.uforms,name='uforms'),
               path('uresult',views.uresult,name='uresult'),
               path('edit_university/<int:pk>/', views.edit_university, name='edit_university'),
               path('delete_university/<int:pk>/', views.delete_university, name='delete_university'),
               path('bforms',views.bforms,name='bforms'),
               path('bresult',views.bresult,name='bresult'),
               path('edit_branch/<int:pk>/', views.edit_branch, name='edit_branch'),
               path('delete_branch/<int:pk>/', views.delete_branch, name='delete_branch'),
                path('eforms',views.eforms,name='eforms'),
               path('eresult',views.eresult,name='eresult'),
               path('edit_employee/<int:pk>/', views.edit_employee, name='edit_employee'),
               path('delete_employee/<int:pk>/', views.delete_employee, name='delete_employee'),
               path('lforms',views.lforms,name='lforms'),
               path('lresult',views.lresult,name='lresult'),
               path('edit_list/<int:pk>/', views.edit_list, name='edit_list'),
               path('delete_list/<int:pk>/', views.delete_list, name='delete_list'),
               path('sforms',views.sforms,name='sforms'),
               path('sresult',views.sresult,name='sresult'),
               path('edit_student/<int:pk>/', views.edit_student, name='edit_student'),
               path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
                path('home', views.home, name='home'),
                path('LoginPage', views.LoginPage, name='LoginPage'),
            
                path('ceresult',views.ceresult,name='ceresult'),
             path('ceforms',views.ceforms,name='ceforms'),
              path('edit_create_employee/<int:pk>/', views.edit_create_employee, name='edit_create_employee'),
              path('delete_create_employee/<int:pk>/', views.delete_create_employee, name='delete_create_employee'),
               path('navbar',views.navbar,name='navbar'),
                path('',views.home,name='home'),
                path('about',views.about,name='about'),
                path('courses',views.courses,name='courses'),
                path('collage',views.collage,name='collage'),
                path('gallery',views.gallery,name='gallery'),
                path('contact',views.contact,name='contact'),
                






















]  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

