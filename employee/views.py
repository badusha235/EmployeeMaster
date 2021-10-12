from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView,ListView,DeleteView,DetailView,UpdateView




class Base(TemplateView):
    template_name="index.html"
