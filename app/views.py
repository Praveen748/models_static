from django.shortcuts import render

# Create your views here.
def dummy(request):
    return render(request,'dummy.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def registration(request):
    return render(request,'registration.html')
