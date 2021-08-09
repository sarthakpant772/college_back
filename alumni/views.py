from django.shortcuts import render,redirect

from . import models
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
        photo=request.POST['photo']

        ins=models.socials(name=name,linkdin_url=link,Company_name=position,Company_post=batch,photo=photo)
        ins.save()
        return redirect('alumni_page')
    else:

        return render(request,'alumni_form.html')