from django.http.response import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
from.models import Departments,Doctors,Contact
from.forms import BookingForm

# Create your views here.

def homepage(request):
# creating dictionary name is numbers using elif loop
#    numbers = {
#     'num' : 10
#    }

#    using forloop  
    #  numbers ={
    #     'num1':{'orange','apple','pappaya','banana'}
    #  }

     return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def booking(request):
    if request.method == 'POST':
        form =BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'booking_messege.html')
    form = BookingForm()
    dict_form = {
        'form' : form
    }

    return render(request, 'booking.html',dict_form)




def doctors(request):
    dict_docs = {
        'doctors' : Doctors.objects.all()
    }
    return render(request, 'doctors.html',dict_docs)



def contact(request):
    # if request.method == 'POST':
    #     form =ContactForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    return render(request, 'contact.html')



def department(request):
    dict_dept = {
        'dept': Departments.objects.all()
    }

    return render(request,'department.html',dict_dept)


# def booking_messege(request):
#     return render(request,'booking_messege.html')