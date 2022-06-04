from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Datas
# Create your views here.
def home(request):
    mydata=Datas.objects.all()
    if(mydata!=''):
        return render(request,"home.html",{'datas':mydata})
    else:
        return render(request,"home.html")
    # return render(request,"home.html")

def addData(request):#http://127.0.0.1:8000/addData
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        obj=Datas()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Mail=mail
        obj.save()
        return redirect('home')
    return render(request,"home.html")

def updateData(request,id):#http://127.0.0.1:8000/updateData
    mydata=Datas.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        mydata.Name=name
        mydata.Age=age
        mydata.Address=address
        mydata.Contact=contact
        mydata.Mail=mail
        mydata.save()
        return redirect('home')

    return render(request,'update.html',{'data':mydata})


def deleteData(request,id):#http://127.0.0.1:8000/deleteData
    mydata=Datas.objects.get(id=id)
    mydata.delete()
    return redirect('home')










    # return render(request,"home.html")

# def product(request):
#     mobile=int(request.GET["mobile"])
#     keyborad=int(request.GET["keyborad"])
#     moniter=int(request.GET["moniter"])
#     price=mobile+keyborad+moniter
#     return render(request,"result.html",{'Price':price})

# def register(request):
#     name=request.POST['name']
#     password=request.POST['password']
#     address=request.POST['address']
#     mail=request.POST['mail']
#     context={
#         'Name':name,
#         'Password':password,
#         'Address':address,
#         'Mail':mail
#         }
#     return render(request,"output.html",context)
#     # 'Name':name,'Password':password,'Address':address,'Mail':mail