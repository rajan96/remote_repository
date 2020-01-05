from django.shortcuts import render,redirect
from djapp.forms import RegistrationForm,LoginForm,FeedbackForm
from django.http.response import HttpResponse
from djapp.models import RegistrationData,feedbackData

# Create your views here.
def Registration_view(request):
    if request.method=="POST":
        rform=RegistrationForm(request.POST)

        if rform.is_valid():
            fname=request.POST.get('First_Name')
            lname=request.POST.get('Last_Name')
            uname=request.POST.get('User_Name')
            pwd=request.POST.get('Password')
            mobile=request.POST.get('Mobile')
            email=request.POST.get('Email_id')
            data=RegistrationData(
                First_Name=fname,
                Last_Name=lname,
                User_Name=uname,
                Password=pwd,
                Mobile=mobile,
                Email_id=email
                )
            data.save()
            rform = RegistrationForm()
            return render(request, 'myapp/reg.html', {'ABCD': rform})
        else:
             return HttpResponse('USer Invalid Data')
    else:
        rform=RegistrationForm()
        return render(request,'myapp/reg.html',{'ABCD':rform})
def Login_View(request):
    if request.method =="POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname = request.POST.get('User_Name')
            pwd = request.POST.get('Password')

            user = RegistrationData.objects.filter(User_Name=uname)
            password = RegistrationData.objects.filter(Password=pwd)

            if user and password:
                return redirect('/home/')
                #return HttpResponse("Success")
            else:
                return HttpResponse("Fail")
        else:
            return HttpResponse('User Invalid Data')
    else:
        rform = LoginForm()
        return render(request,'myapp/login.html',{'ABCD':rform})

def home_view(request):
    return render(request,'myapp/home.html')

from djapp.forms import ContactForm
from djapp.models import contactData
def contact_view(request):
    if request.method=="POST":
        cform=ContactForm(request.POST)
        if cform.is_valid():
            name=request.POST.get('name')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')

            courses=cform.cleaned_data.get('courses')
            trainer=cform.cleaned_data.get('trainer')
            branches=cform.cleaned_data.get('branches')
            date=cform.cleaned_data.get('date')
            gender=cform.cleaned_data.get('gender')
            data=contactData(
                name=name,
                mobile=mobile,
                email=email,
                courses=courses,
                trainer=trainer,
                branches=branches,
                date=date,
                gender=gender
            )
            data.save()
            cform=ContactForm()
            return  render(request,'myapp/contact.html',{'cform':cform})
        else:
            return HttpResponse('User Invalid Data')
    else:
        cform=ContactForm()
    return render(request,'myapp/contact.html',{'cform':cform})

from djapp.models import coursesData
def services_view(request):
    courses=coursesData.objects.all()
    return render(request,'myapp/services.html',{'courses':courses})

def gallery_view(request):
    return render(request,'myapp/gallery.html')

import datetime as dt
date1=dt.datetime.now()
def feedback_view(request):
    if request.method=="POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')

            data=feedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fform=FeedbackForm()
            data=feedbackData.objects.all()
            return render(request,'myapp/feedback.html',{'fform':fform,'data':data})
        else:
            return HttpResponse("User Missed some values")
    else:
        data=feedbackData.objects.all()
        fform=FeedbackForm()
        return render(request,'myapp/feedback.html',{'fform':fform,'data':data})


