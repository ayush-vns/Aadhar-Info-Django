from django.shortcuts import render, HttpResponse, redirect
# from models import aadharMOdels




def information (request):        
    return render(request, "information.html")