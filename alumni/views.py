from django.shortcuts import render
from . import models
# Create your views here.
def alumni_page(request):
    alunis= models.socials.objects.all()
    alumnies = { 'alunis' : alunis }
    return render(request,'alumni.html', alumnies)
