from django.urls import path
from adminpanel import views

urlpatterns=[
    path("addemployee/",views.EmployeeView.as_view(),name="addemployee"),
    path("home/",views.Home.as_view(),name="home"),
    path("dashboard/",views.Dashboard.as_view(),name="dashboard"),
    path("employee_table/",views.ViewEmployee.as_view(),name="employetable"),
    path("employeegalary/",views.EmployeGalary.as_view(),name="empgalary"),
    path("employeeDelete/<int:pk>",views.Delete.as_view(),name="delete"),
    path("viewemployee/<int:pk>",views.ViewEmployeeGalary.as_view(),name="viewemp"),
    path("update/<int:pk>",views.UpdateEmployee.as_view(),name="update"),
    path("skills/",views.Skills.as_view(),name="skills"),
    path("",views.User_login,name="login"),
    path("registration",views.registration_view,name='registration'),
    path("logout",views.signout,name="logout")
    
    
]