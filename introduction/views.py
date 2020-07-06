from django.shortcuts import render

# Create your views here.
def main(request) :
    return render(request, 'introduction/main.html')
def sacai(request) :
    return render(request, 'introduction/sacai.html')
def supreme(request) :
    return render(request, 'introduction/supreme.html')
def stussy(request) :
    return render(request, 'introduction/stussy.html')   