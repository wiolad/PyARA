from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'resources/index.html')
#    return HttpResponse('Welcome to PyARA - Python Amazing Resources App!')
