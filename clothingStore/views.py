from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Clothing
from .forms import RegistrationForm, RegistrationModal
from .models import RegistrationData
from django.contrib import messages
# Create your views here.


def Home(request):

    context = {
        "name": "Thuytran",
        "number":"123456"
    }

    return render(request,'home.html',context)


def Clothings(request):
    obj = Clothing.objects.get(id=1)

    context = {
        "list": ["Outwear","Swimwear","Sportwear","Underwear"],
        "mynum": 50,
        "data": obj
    }
    return render(request,'clothing.html',context)


def Newsdate(request, year):
    cloth_list = Clothing.objects.filter(pub_date__year=year)
    context ={
        'year': year,
        'cloth_list': cloth_list
    }

    return render(request,'newsdate.html',context)


def Contact(request):
    return render(request,'contact.html')


def Register(request):

    context = {
        "form":RegistrationForm
    }
    return render(request,'signup.html',context)


def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        my_register=RegistrationData(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    email=form.cleaned_data['email'],
                                    phone=form.cleaned_data['phone']
                                  )
        my_register.save()
        messages.add_message(request, messages.SUCCESS,'You have signup successfully!!!')
    return redirect('SignUp')


def modalForm(request):
    context = {
        "modalform": RegistrationModal
    }
    return render(request,'modalForm.html',context)


def addModalForm(request):
    mymodalform = RegistrationModal(request.POST)
    print(mymodalform.is_valid())
    if mymodalform.is_valid():
        mymodalform.save()
        messages.add_message(request, messages.SUCCESS, 'You have signup successfully!!!')
    return redirect('modalForm')