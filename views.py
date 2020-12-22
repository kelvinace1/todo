from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(requests):
    context = {
        'posts':Post.objects.all()
    }
    return render(requests, "ad/home.html", context)

def todo(request):
    new = Post(content = request.POST['content'])
    new.save()
    return redirect('home')

def delete(request, pk):
    new = Post.objects.get(id=pk)
    new.delete()
    return redirect('home')
