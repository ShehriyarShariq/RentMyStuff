from django.shortcuts import render, redirect

# Create your views here.
def index(request):
        return render(request, "index.html")

def about(request):
        return render(request, "about.html")

def contact(request):
        return render(request, "contact.html")

def dummy(request):
        return render(request, "dummy.xml")
