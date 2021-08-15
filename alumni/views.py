from django.shortcuts import render,redirect
from .forms import alumni_forms
from . import models
from django.contrib import messages
# Create your views here.
def alumni_page(request):
    alunis= models.socials.objects.all()
    alumnies = { 'alunis' : alunis }
    return render(request,'alumni.html', alumnies)


def alumni_form(request):
    if request.method=="POST":
        name=request.POST['name']
        position=request.POST['position']
        batch=request.POST['batch']
        link=request.POST['link']
        photo=request.FILES.get('photo',None)
        alunis= models.socials.objects.all()
        alumnies = { 'alunis' : alunis }
        flag=0
        # if batch-'0'>2023 and batch-'0'<2009:
        #     messages.info(request,'This Batch not permited')
        #     return redirect('alumni_form')
        for alumni in alunis:
            if(alumni.linkdin_url==link):
                flag=1
                break
        if(flag!=1):
            ins=models.socials(name=name,linkdin_url=link,Company_name=position,Company_post=batch,photo=photo)
            ins.save()
            return redirect('alumni_page')
        else:
            messages.info(request,'Linkedin-URL already Taken')
            return redirect('alumni_form')    
    else:

        return render(request,'alumni_form.html')