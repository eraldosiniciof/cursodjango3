from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello World, se escrever <b>qualquer</b> <u>coisa</u> aparece aqui')
