from django.shortcuts import render

# Create your views here.
def main3(request) :
    return render(request, 'sports/main3.html')
def airmax(request) :
    return render(request, 'sports/airmax.html')
def jordan(request) :
    return render(request, 'sports/jordan.html')