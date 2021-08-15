from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'home_page.html')

def aboutus(request):
    return render(request,'about_us.html')

def club(request):
    return render(request,'club.html')
