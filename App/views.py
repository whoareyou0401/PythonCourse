from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.cache import cache
# Create your views here.
from .gongju import my_str
import logging

logger=logging.getLogger('django')
def email(requset):
    title='你很帅'
    neirong='你超级无敌帅'
    fajianren = '847159953@qq.com'
    shoujianren=[
        '872898324@qq.com'
    ]
    send_mail(title,neirong,fajianren,shoujianren)
    return HttpResponse('ok')

def yemian(req):
    logger.info('lalal')
    title = '小哥哥,288了解一下'
    neirong = '288了解一下'
    fajianren = '847159953@qq.com'
    shoujianren = [
        '1752641276@qq.com'
    ]
    tmp=loader.get_template('email.html')
    h=tmp.render()
    send_mail(title, neirong, fajianren, shoujianren,html_message=h)
    return HttpResponse('ok')


def zhuce(requset):
    if requset.method=='GET':
        return render(requset,'zhuce.html')
    else:
        mail=requset.POST.get('email')
        title = '小哥哥,288了解一下'
        neirong = '288了解一下'
        fajianren = '847159953@qq.com'
        shoujianren = [
          mail
        ]
        random_str=my_str()

        url='http://120.79.93.72:12377/App/jihuo/'+random_str
        tam=loader.get_template('email.html')
        html=tam.render({"url":url})
        send_mail(title,neirong,fajianren,shoujianren,html_message=html)
        cache.set(random_str,email,120)
        return HttpResponse('ok')

def jihuo(requset,random_str):

    huan=cache.get(random_str)
    if huan:
        return HttpResponse('ok')
    else:
        return HttpResponse("no")