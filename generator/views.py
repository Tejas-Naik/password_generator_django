from django.shortcuts import render
import random 

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {"password": "saldjf452"})

def password(request):

    characters = 'qwertyuiopasdfghjklzxcvbnm'

    length = 10

    thepassword = ''
    for i in range(length):
        thepassword +=  random.choice(characters)
        

    return render(request, 'generator/password.html', {'password':thepassword})