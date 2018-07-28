# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from . models import Item
from ..validation.models import User

# Create your views here.

def home(request):
    try:
        request.session['user']
    except KeyError:
        messages.error(request, 'Must be logged in to view information')
        return redirect(reverse('validation:login'))
    user_id = int(request.session['user'])
    context = {
        'currentUser': User.objects.get(id=user_id),
        'userList': Item.objects.getUsersItems(user_id),
        'availItems': Item.objects.getAvailableItems(user_id)

    }
    return render(request, 'add_items/index.html', context)

def addItem(request):
    if request.method == 'POST':
        valItem = Item.objects.checkItem(request.POST)
        if valItem:
            item = Item.objects.makeItem(request.POST)
            print item.id
            Item.objects.addToList(request.POST['user_id'],item.id)
            return redirect(reverse('additems:home'))
        else:
            messages.error(request, 'Item must be two or more characters long')
            return redirect(reverse('additems:create'))
    else:
        return redirect(reverse('additems:home'))

def deleteItem (request, id):
    try:
        request.session['user']
    except KeyError:
        messages.error(request, 'Must be logged in to view')
        return redirect(reverse('validation:login'))
    Item.objects.deleteItem(id)
    return redirect(reverse('additems:home'))

def addToList(request, id):
    try:
        request.session['user']
    except KeyError:
        messages.error(request, 'Must be logged in to view')
        return redirect(reverse('validation:login'))
    Item.objects.addToList(request.session['user'], id)
    return redirect(reverse('additems:home'))

def removeFromList(request, id):
    try:
        request.session['user']
    except KeyError:
        messages.error(request, 'Must be logged in to view')
        return redirect(reverse('validation:login'))
    Item.objects.removeFromList(request.session['user'], id)
    return redirect(reverse('additems:home'))

def item(request, id):
    try:
        request.session['user']
    except KeyError:
        messages.error(request, 'Must be logged in to view')
        return redirect(reverse('validation:login'))
    context = {
        'users': Item.objects.getUsers(id)
    }
    return render(request, 'add_items/item.html', context)

def create(request):
    try:
        request.session['user']
    except KeyError:
        messages.error(request, 'Must be logged in to view')
        return redirect(reverse('validation:login'))
    return render(request, 'add_items/create.html')