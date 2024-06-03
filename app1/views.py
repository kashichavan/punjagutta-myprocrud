from django.shortcuts import render,redirect
from .forms import CarForm
from .models import CarModel
# Create your views here.

def create(request):
    if request.method=='POST':
        form = CarForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/getdata/')
    return render(request,'create.html')

def getdata(request):
    datas=CarModel.objects.all()
    d={
    'data':datas
    }
    return render(request,'getdata.html',context=d)

def update(request,id):
    obj=CarModel.objects.get(id=id)
    if request.method=="POST":
        form=CarForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/getdata/')
    return render(request,'update.html',{'data':obj})

def delete(request,id):
    obj=CarModel.objects.get(id=id)
    obj.delete()
    return redirect('/getdata/')
