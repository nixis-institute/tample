from django.shortcuts import render

# Create your views here.

def homepage(request):
    if(request.method=="POST"):
        data = dict(request.POST)
        query = data["search"][0]
        print(query)
    return render(request,'home.html')
