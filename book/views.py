from django.shortcuts import render

# Create your views here.
def Temp (request):
    return render(request,'temp.html')