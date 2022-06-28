import email
from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html') 

def admin_index(request):
    return render(request,'Admin_Template/A_index.html')


