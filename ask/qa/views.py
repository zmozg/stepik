#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def test(request, *args, **kwargs):
    response = HttpResponse('OK from qa or DJANGO')
    #print(request.META)
    #response['ATta'] = 'OK'
    #response = request.META.get('HTTP_USER_AGENT')
    #response = request.META.get('REMOTE_ADDR')
    response.set_cookie('visited','OK')
    print(request.COOKIES)

    #return HttpResponse(response,)
    return render(request, 'qa/base.html',{
    'test': response,
    })

def decor(func):
    print('krasota')
    func()
    print('lepota')
    return func

def mego_decor(funci):
    print('OGO')
    funci()
    print('NICHOSI')
    return funci

#@mego_decor
#@decor
def simple():
    print('nu prosto')
    return
