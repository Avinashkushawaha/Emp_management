from django.shortcuts import render, redirect
from .models import Emp
# Create your views here.
def home(request):
    emps=Emp.objects.all()
    return render(request,'emp/home.html',{'emps':emps})

def add_emp(request):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address 
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True 

        e.save()       

        return redirect("/home")
    return render(request, "emp/add_emp.html")

def delete_emp(request, emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("home")

def update_emp(request, emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request, "emp/update_emp.html", {'emp':emp})


def do_update_emp(request, emp_id_temp):
    if request.method=='POST':
     emp_name=request.POST.get("emp_name")
     emp_id=request.POST.get("emp_id")
     emp_phone=request.POST.get("emp_phone")
     emp_address=request.POST.get("emp_address")
     emp_working=request.POST.get("emp_working")
     emp_department=request.POST.get("emp_department")   

     e=Emp.objects.get(pk=emp_id_temp)
     e.name=emp_name
     e.emp_id=emp_id
     e.phone=emp_phone
     e.address=emp_address 
     e.department=emp_department
     if emp_working is None:
        e.working=False
     else:
        e.working=True
     e.save()   
    return redirect("/home")