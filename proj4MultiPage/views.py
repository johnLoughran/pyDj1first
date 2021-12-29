from django.shortcuts import render
from . import mathFns

def home(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html')

def result(request):
    user_input = request.GET['userInput']
    user_input = mathFns.square(user_input)
    return render(request, 'result.html', {'inputFromHome': user_input })

'''
def result(request):
    if(request.GET['userInput']):
        user_input = request.GET['userInput']
        return render(request, 'result.html', {'inputFromHome': user_input })
    else :
        return render(request, 'result.html')
'''
