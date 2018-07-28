from django.shortcuts import render

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from models import User
# Create your views here.
def index(request):
    return render(request, 'validation/index.html')

def validateUser(request, route):
    if request.method == 'POST':
        if route == 'reg':
            print request.POST
            newUser = User.objects.newUser(request.POST)
        else:
            newUser = User.objects.validateUser(request.POST)
            print newUser
        if not newUser[1]:
            for x in range(len(newUser[0])):
                messages.error(request, newUser[0][x])
            return redirect(reverse('validation:login'))
        else:
            request.session['user'] =newUser[0].id
            return redirect(reverse('additems:home'))
    else:
        return redirect(reverse('validation:login'))

def logOut (request):
    request.session.clear()
    messages.add_message(request, messages.INFO,"You have been logged out!", extra_tags='logout')
    return redirect(reverse('validation:login'))