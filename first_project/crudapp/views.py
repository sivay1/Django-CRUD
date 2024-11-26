from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Details 
# Create your views here.
def home(request):
    
    if request.method == "POST":
        username = request.POST["name"]
        userage = request.POST["age"]
        usergender = request.POST["gender"]
        Details.objects.create(name=username,age=userage,gender=usergender)

        return redirect("home")
    else:
        return render(request, 'createuser.html')
    
def view(request):
    view_data = Details.objects.all()
    return render(request,"viewuser.html",{"view_data":view_data})

def update_user(request,id):
    update_user = Details.objects.get(id=id)
    if request.method == "POST":
        update_user.name = request.POST["name"]
        update_user.age = request.POST["age"]
        update_user.gender = request.POST["gender"]
        update_user.save()
        return redirect("view")
    else:
        return render(request, "updateuser.html", {"update_user":update_user})

def delete_user(request,id):
    del_user = Details.objects.get(id=id)
    del_user.delete()
    return redirect("view")