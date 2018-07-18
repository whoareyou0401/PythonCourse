from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, send_mass_mail
from django.template import loader
from .my_util import get_random_str

# Create your views here.

def send_my_email(req):
    title = "阿里offer"
    msg = "恭喜你做了个白日梦"
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        '3207196028@qq.com'
    ]
    # 发送邮件
    send_mail(title, msg, email_from, reciever)
    return HttpResponse("ok")

def send_email_v1(req):
    title = "阿里offer"
    msg = " "
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        '3207196028@qq.com'
    ]
    # 加载模板
    template = loader.get_template('email.html')
    # 渲染模板
    html_str = template.render({'msg': "老铁666"})

    # 发送邮件
    send_mail(title, msg, email_from, reciever, html_message=html_str)
    return HttpResponse("ok")

def verify(req):
    if req.method == "GET":
        return render(req, "verify.html")
    else:
        param = req.POST
        email = param.get("email")
        # 生成随机字符
        random_str = get_random_str()
        # 拼接验证连接
        url = "http://118.24.95.20:8003/t8/active" + random_str
        # 加载激活模板
        tmp = loader.get_template('active.html')
        # 渲染
        html_str = tmp.render({'url': url})

        # 准备邮件数据
        title = "阿里offer"
        msg = " "
        email_from = settings.DEFAULT_FROM_EMAIL
        reciever = [
           # email,
            '3207196028@qq.com'
        ]
        send_mail(title, msg, email_from, reciever, html_message=html_str)
        # 记录 token对应的邮箱是谁
        cache.set(random_str, email, 120)
        return HttpResponse("ok")

def active(req, random_str):
    res = cache.get(random_str)
    if res:
        return HttpResponse(res+"激活成功")
    else:
        return HttpResponse("验证连接无效")

def send_many_email(req):
    title = "阿里offer"
    content1 = "感谢参与！！！"
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever1 = [
        '3207196028@qq.com'
    ]
    content2 = "well done!!!"
    msg1 = (title, content1, email_from, reciever1)
    msg2 = ("小伙子", content2, email_from, ['3207196028@qq.com'])

    send_mass_mail((msg1, msg2), fail_silently = True)

    return HttpResponse("ok")