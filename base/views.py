from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# can be function based or class based 

rooms = [
    {'id': 1, 'name':'Lets learn python!'},
    {'id': 2, 'name':'Lets learn javascript!'},
    {'id': 3, 'name':'backend developers'}
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
