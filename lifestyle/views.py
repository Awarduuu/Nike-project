from django.shortcuts import render

# Create your views here.
def main2(request) :
    return render(request, 'lifestyle/main2.html')
def daybreak(request) :
    return render(request, 'lifestyle/daybreak.html')
def blazer(request) :
    return render(request, 'lifestyle/blazer.html')
