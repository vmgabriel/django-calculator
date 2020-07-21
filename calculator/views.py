# Develop: vmgabriel

"""Module for Views of Calculator"""

from django.shortcuts import render
from django.http import HttpResponse


def show_calculator(request):
    """Show Calculador of URI"""
    template = 'main.html'
    if 'display' not in request.GET or request.GET['display'] == '':
        return render(request, template)
    operation = request.GET['display']
    try:
        result = eval(operation)
        print('result - {}'.format(result))
        return render(request, template, {'result': result})
    except ZeroDivisionError:
        return render(request, template, {
            'result': '',
            'error': {
                'title': 'Error in Division',
                'description': 'Not Valid Division For Zero'
            }
        })
    except SyntaxError:
        return render(request, template, {
            'result': '',
            'error': {
                'title': 'Error in Sintax',
                'description': 'Sintax not Valid, verify data'
            }
        })
    except Exception as err:
        print('excepcion - {}'.format(err))
        return render(request, template, {'result': result})
