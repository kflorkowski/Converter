from django.shortcuts import render

# Create your views here.
def distance_conversion(request):
    return render(request, 'distance_converter.html')

def weight_conversion(request):
    return render(request, 'weight_converter.html')

def temperature_conversion(request):
    return render(request, 'temperature_converter.html')
