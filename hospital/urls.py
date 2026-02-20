"""
URL configuration for lifehospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('404/', views.error, name='404.html'),
    path('hospital/', views.about, name='hospital.html'),
    path('contact/', views.contact, name='contact.html'),
    path('appointment/', views.appointment, name='appointment.html'),
    path('departmentdetails/', views.department_details, name='department-details.html'),
    path('departments/', views.departments, name='departments.html'),
    path('doctors/', views.doctors, name='doctors.html'),
    path('faq/', views.faq, name='faq.html'),
    path('gallery/', views.gallery, name='gallery.html'),
    path('index/', views.index, name='index.html'),
    path('privacy/', views.privacy, name='privacy.html'),
    path('terms/', views.terms, name='terms.html'),
    path('servicedetails/', views.service_details, name='service-details.html'),
    path('services/', views.services, name='services.html'),
    path('starterpage/', views.starter_page, name='starter-page.html'),
    path('testimonials/', views.testimonials, name='testimonials.html'),
    path('about/', views.about, name='about.html'),



]
