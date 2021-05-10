from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'website/into.html')


def room(request, room_name):
    return render(request, 'website/room.html', {'room_name': room_name})