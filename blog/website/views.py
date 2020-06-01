from django.shortcuts import render

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

    data = {
        'name': 'curso de django 3',
        'lista_tecnologia': lista
    }

    return render(request, 'index.html', data)
