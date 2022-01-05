from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from .models import Data


class DataListView(ListView):
    model = Data
