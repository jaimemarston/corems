from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import *

class C110ListView(generic.ListView):
    model = C110
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(C110ListView, self).get_context_data(**kwargs)
        
        return context