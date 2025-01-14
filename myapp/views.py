from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Test

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World")

def greet(request, name):
    return HttpResponse(f"Hi! {name}, Greetings for the day!")

def dashboard(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        unit = request.POST.get('unit')
        Test.objects.create(name=name,age=age,unit=unit)
        return redirect('dashboard')
    # Fetch all employee data
    else:
        res = Test.objects.all()
        data = []
        for i in res:
            emp_data = {
                'id': i.id,
                'name': i.name,
                'age': i.age,
                'unit': i.unit,
            }
            data.append(emp_data)
        
        context = {'data': data}  # Pass the data to the template
        return render(request, 'index.html', context)



def edit_emp(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        unit = request.POST.get('unit')

        # Update the employee data in the database
        Test.objects.filter(pk=id).update(name=name, age=age, unit=unit)
        
        # Redirect to dashboard after updating
        return redirect('dashboard')

    else:
        # If the method is GET, fetch the employee details to edit
        id = request.GET.get('id')
        emp_data = Test.objects.get(pk=id)
        
        context = {
            'id': id,
            'name': emp_data.name,
            'age': emp_data.age,
            'unit': emp_data.unit,
        }
        
        return render(request, 'edit.html', context)

