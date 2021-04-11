from django.shortcuts import render

from django.http import HttpResponse
from .bmi import bmi_cal
from .retirement import ret

# Create your views here.

def homepage(request):
    return render(request=request, template_name= "bmi_cal/home.html")

def bmi(request):

    try:
        feet = request.POST.get('feet')
        inch = request.POST.get('inch')
        weight = request.POST.get('weight')
        if feet is None or inch is None or weight is None:
            data = "Please fill all the boxes"
            return render(request= request, template_name="bmi_cal/bmi.html", context={'data':data})
        else:
            feet = int(feet)
            inch = int(inch)
            weight = float(weight)
            a = bmi_cal()
            data = a.calculate_bmi(feet,inch,weight)
            print(data)
            return render(request=request, template_name= "bmi_cal/bmi.html", context= {'data':data})
    except:
        data = "Please fill all the boxes"
        return render(request=request, template_name= "bmi_cal/bmi.html", context= {'data':data})

def retr(request):
    try:
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        percent = request.POST.get('percent')
        target = request.POST.get('target')
        if age is None or salary is None or percent is None or target is None:
            data = "Please fill all the boxes"
            return render(request= request, template_name="bmi_cal/ret.html", context={'data':data})
        else:
            age = int(age)
            salary = int(salary)
            percent = float(percent)
            target = int(target)
            b = ret()
            data = b.retirement_cal(age,salary,percent,target)
            print(data)
            return render(request=request, template_name= "bmi_cal/ret.html", context= {'data':data})
    except:
        data = "Please fill all the boxes"
        return render(request=request, template_name= "bmi_cal/ret.html", context= {'data':data})
    return render(request=request, template_name="bmi_cal/ret.html")