from django.shortcuts import render
from .models import Post

def hello_blog(request):
    lista = [
        'Django',
        'Python',
        'Git',
        'Html',
        'Banco de Dados',
        'Linux',
        'Nginx',
        'Uwsgi',
        'Systemctl'
    ]

    list_posts = Post.objects.all()

    data = {
        'name': 'curso de django 3',
        'lista_tecnologia': lista,
        'posts': list_posts
    }


    return render(request, 'index.html', data)
