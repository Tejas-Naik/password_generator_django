from django.shortcuts import render
import random 

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {"password": "saldjf452"})

def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))    
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_'))


    length = int(request.GET.get('length', 12))

    thepassword = ''
    for i in range(length):
        thepassword +=  random.choice(characters)
        

    return render(request, 'generator/password.html', {'password':thepassword})