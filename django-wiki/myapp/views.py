from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "title" : "Index page for CSUCHICO WIKI"
    }
    return render(request,"base.html", context = context)