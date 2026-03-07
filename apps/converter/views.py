from django.shortcuts import render

def converter_view(request):
    return render(request, 'converter/converter.html') 
