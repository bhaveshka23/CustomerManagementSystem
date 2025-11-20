from django.shortcuts import render,redirect
from .models import Customer
import datetime

def validate_date(value):
    dob_date = datetime.datetime.strptime(value, "%Y-%m-%d").date()
    today = datetime.date.today()

    return dob_date > today 

def DisplayCustomer(request):
    users = Customer.objects.all()
    return render(request,'DisplayCust.html',{'users':users})

def AddCustomer(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        department = request.POST.get('department')
        image = request.FILES.get('image')

        print(name,contact,gender,dob,address,department)

        if not name:
            return render(request,'AddCust.html',{'error':'Name is Required..!'})
        
        if (validate_date(dob)):
            return render(request,'AddCust.html',{'error':'Date of birth is invalid!'})
        
        if len(contact) > 10:
            return  render(request,'AddCust.html',{'error':'Contact No. is invalid'})

        
        Customer.objects.create(
            Cst_name = name,
            Cst_contact=contact,
            Cst_gender=gender,
            Cst_dob = dob,
            Cst_photo = image,
            Cst_address = address,
            Cst_department = department

        )

        return redirect('DisplayCustomers')

    return render(request,'AddCust.html',{'error':''})

def UpdateCustomer(request,Cst_id):

    customer = Customer.objects.get(Cst_id = Cst_id)

    if request.method == "POST":
        customer.Cst_name = request.POST.get('name')
        customer.Cst_contact = request.POST.get('contact')
        customer.Cst_gender = request.POST.get('gender')
        customer.Cst_dob = request.POST.get('dob')
        customer.Cst_address = request.POST.get('address')
        customer.Cst_department = request.POST.get('department')

        if request.FILES.get('image'):
            customer.Cst_photo = request.FILES.get('image')

        customer.save()
        return redirect("DisplayCustomers") 

    return render(request,'UpdateCust.html',{'customer': customer})


def DeleteCustomer(request,Cst_id):
    customer = Customer.objects.get(Cst_id=Cst_id)
    customer.delete()
    return redirect("DisplayCustomers")