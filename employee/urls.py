from django.urls import path
from django import views
from employee import views

urlpatterns=[
    path("homee",views.Base.as_view(),name="homee")
   
    
]