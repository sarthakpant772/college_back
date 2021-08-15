from alumni import models
from django.shortcuts import render,redirect
from . import models
# Create your views here.
def store(request):
    store_details=models.Store.objects.all()
    store_d={'store_details':store_details}
    return render(request,'selling.html',store_d)  

def store_form(request):
    if request.method=="POST":
        title=request.POST['title']
        para=request.POST['para']
        email=request.POST['email']
        image=request.FILES.get('image',None)
        ins=models.Store(title=title,para=para,email=email,image=image)
        ins.save()
        return redirect('store')
    else:    
        return render(request,'store_form.html') 