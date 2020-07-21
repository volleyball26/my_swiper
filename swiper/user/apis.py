from django.http import JsonResponse
from django.shortcuts import render


def fetch(request):
    phonenum = request.GET.get('phonenum')
    print(phonenum)
    data = {
        'code': 0,
        'data': 'null'
    }
    return JsonResponse(data=data)