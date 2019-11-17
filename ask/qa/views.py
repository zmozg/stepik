#from django.shortcuts import render
from django.http import HttpResponse

def test(request, *args, **kwargs):
    response = HttpResponse('OK from qa or DJANGO')
    #print(request.META)
    #response['ATta'] = 'OK'
    #response = request.META.get('HTTP_USER_AGENT')
    #response = request.META.get('REMOTE_ADDR')
    response.set_cookie('visited','OK')
    print(request.COOKIES)

    #return HttpResponse(response,)
    return response
