from django.shortcuts import render
from . models import Employee, Contact
from . forms import EmployeeForm
from django.contrib import messages

# Create your views here.
def showTest(request):
    return render(request, 'emp/test.html')

def empForm(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        form.save()
        messages.success(request, 'Employee added successfully!!!')
        form = EmployeeForm()
        return render(request, 'emp/emp.html', {'form':form})
    else:
        form = EmployeeForm()
        return render(request, 'emp/emp.html', {'form':form})
    
def listEmps():
    emps = Employee.objects.all()
    return emps

def showEmpList(request):
    emps = listEmps()
    return render(request, 'emp/list.html', {'emplist': emps})

def delEmp(request, id):
    e = Employee.objects.get(pk=id)
    e.delete()
    messages.error(request, 'Employee deleted successfully!!!')
    emps = listEmps()
    return render(request, 'emp/list.html', {'emplist': emps})

def updateEmpById(request, id):
    e = Employee.objects.get(pk=id)
    form = EmployeeForm(request.POST or None, instance=e)
    if request.method == 'POST':
        form.save()
        emps = listEmps()
        return render(request, 'emp/list.html', {'emplist': emps})
    
    return render(request, 'emp/update.html', {'form': form})

def contactForm(request):
    if request.method == 'POST':
        name = request.POST['name1']
        email = request.POST['email']
        contact = request.POST['contact']
        data = Contact.objects.create(
            name = name,
            email = email,
            contact = contact
        )
        data.save()
        messages.success(request, 'Thank you for contacting us!!')

    return render(request, 'emp/contact.html')