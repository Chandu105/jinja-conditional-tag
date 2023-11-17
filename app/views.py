from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':400,'b':900,'c':8000}
    return render(request,'conditions.html',d)