from django.shortcuts import render

# Create your views here.
from .models import Post 

def blogView(request):
    lista_post = Post.objects.all()

    return render(request, 'index.html', {'lista_post': lista_post})

    