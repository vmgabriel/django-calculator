
"""Module test"""

import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def saludo(request) -> HttpResponse:
    """Greeting"""
    lista = ['un dato - {}'.format(x) for x in range(200)]
    return render(
        request,
        'first_page.html',
        {'nombre_app': 'App Pro', 'datas': lista}
    )


def calcula_edad(request, date: str) -> HttpResponse:
    """This calc"""
    edad_valid = datetime.datetime.now().year
    document = 'Esto pueden ser muchas cosas {}'.format(edad_valid - date)
    return HttpResponse(document)


def json_peticion(request) -> JsonResponse:
    numbers = request.GET['numbers']
    numbers_transform = list(map(lambda x: int(x), numbers.split(',')))
    return JsonResponse({
        'message': 'Hello World',
        'code': 200,
        'numbers': sorted(numbers_transform)
    }, json_dumps_params ={'indent': 4})
