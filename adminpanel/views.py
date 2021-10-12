from django import forms
from django.db import models
from django.shortcuts import redirect, render
from django.views.generic import TemplateView,ListView,DeleteView,DetailView,UpdateView
from adminpanel.forms import EmployeeForm
from django.urls.base import reverse_lazy
import math
from django.contrib.auth import authenticate,login,logout
from adminpanel import forms

from adminpanel.models import EmployeeDetails

# Create your views here.


class EmployeeView(TemplateView):
    model=EmployeeDetails
    template_name="addemployee.html"
    form_class=EmployeeForm
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        return render(request,self.template_name,{"form":form})
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST,files=request.FILES)
        if form.is_valid():
            obj=EmployeeDetails()
            obj.name=form.cleaned_data["name"]
            obj.image=form.cleaned_data["image"]
            obj.email=form.cleaned_data["email"]
           
            obj.phone=form.cleaned_data["phone"]
            obj.address=form.cleaned_data["address"]
            obj.Employment_type=form.cleaned_data["Employment_type"]
            obj.age=form.cleaned_data["age"]
            obj.gender=form.cleaned_data["gender"]
            obj.position=form.cleaned_data["position"]
            obj.save()
            print("saved")

            msg="New Employee Created"
            
            return render(request,self.template_name,{"msg":msg})   
        else:
            print(form.errors)
            return render(request,self.template_name,{"form":form})
            
class Home(TemplateView):
        template_name="base.html"
        


class Dashboard(TemplateView):


    template_name="graph.html"
    model=EmployeeDetails
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        mcount=self.model.objects.filter(gender="male").count()
        fcount=self.model.objects.filter(gender="female").count()
        tcount=self.model.objects.all().count()
        ptime=self.model.objects.filter(Employment_type="parttime").count()
        ftime=self.model.objects.filter(Employment_type="fulltime").count()
        sd=cal(self.model.objects.filter(position="Software Developer").count(),tcount)
        tw=cal(self.model.objects.filter(position="Technical Writer").count(),tcount)
        ps=cal(self.model.objects.filter(position="Associate Supervisor").count(),tcount)
        us=cal(self.model.objects.filter(position="Admissions Counselor").count(),tcount)
        st=cal(self.model.objects.filter(position="Software Tester").count(),tcount)
        
        
       
        


        context["sd"]=sd
        context["tw"]=tw
        context["ps"]=ps
        context["us"]=us
        context["st"]=st
        context["mcount"]=mcount
        context["fcount"]=fcount
        context["tcount"]=tcount
        context["ptime"]=ptime
        context["ftime"]=ftime


        return context
        

class EmployeGalary(ListView):
    model=EmployeeDetails
    template_name="employeegalary.html"
    context_object_name="employees"


class ViewEmployee(ListView):
    model=EmployeeDetails
    template_name="employetable.html"
    context_object_name="employees"

class Delete(DeleteView):
    model=EmployeeDetails
    template_name="delete.html"
    success_url=reverse_lazy("employetable")


class ViewEmployeeGalary(DetailView):
    model=EmployeeDetails
    template_name="viewemployee.html"
    context_object_name="employee"

class UpdateEmployee(UpdateView):
    model=EmployeeDetails
    template_name="updateemployee.html"
    form_class=EmployeeForm
    success_url=reverse_lazy("employetable")

class Skills(TemplateView):
    template_name="dashboard.html"


def cal(i,j):
    j=(i/j)*100
    j=math.trunc(j)
    return j
    


def registration_view(request):
    form=forms.UserRegistrationForm()
    
    context={"form":form}
    if request.method=="POST":
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("login")
        else:
            print(form.errors)
            context["form"]=form
            return render(request,"registration.html",context)


    return render(request,"registration.html",context)


def User_login(request):
    form=forms.SignInForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.SignInForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            
            # ??????????????????????????
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if request.user.is_superuser:
                    return redirect("dashboard")
                return redirect("homee")
            else:
                context["form"]=form
                return render(request,"login.html",context)
    return render(request,"login.html",context)


def signout(request):
    logout(request)
    print("jj")
    return redirect("login")






