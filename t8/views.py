from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, send_mass_mail
from django.template import loader
from .my_util import get_random_str
from django.core.cache import cache
# Create your views here.

# 单条发送短信
def send_my_email(req):
    title = "阿里offer"
    msg = "恭喜您获得美妞一份！"
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        '2226849668@qq.com'
    ]
    # 发送邮件
    send_mail(title, msg, email_from, reciever)
    return HttpResponse("ok")


def send_email_v1(req):
    title = "世界最大BUG王！！！"
    msg = "恭喜您获得大BUG一份！"
    email_from = settings.DEFAULT_FROM_EMAIL
    reciever = [
        '2226849668@qq.com'
    ]
    # 加载模板
    template = loader.get_template('email.html')
    # 加载模板后对模板进行渲染
    html_str = template.render({'msg': '你会写bug你最牛*！'})
    # d打印在后台可看信息
    print(html_str)
    # 发送邮件
    send_mail(title, msg, email_from, reciever, html_message=html_str)
    return HttpResponse("信息发送成功！")


# 邮箱验证
def verify(req):
    if req.method == "GET":
        return render(req, "verify.html")
    else:
        params = req.POST
        email = params.get("email")
        # 生成随机字符，保证每个验证的连接地址不相同，便于处理邮箱是否激活
        random_str = get_random_str()
        # 拼接验证连接
        url = 'http://203.195.168.253:8000/t8/active' + random_str
        # 加载激活模板
        tmp = loader.get_template('active.html')
        # 渲染模板
        html_str = tmp.render({'url': url})

        # 准备邮件数据
        title = "阿里offer"
        msg = " "
        email_from = settings.DEFAULT_FROM_EMAIL
        reciever = [
            email,
        ]
        send_mail(title, msg, email_from, reciever, html_message=html_str)
        # 对缓存做一份信息留存,缓存信息时间120秒
        # 通过生成的随机字符串做键，用邮箱做值，可快速找到给哪个邮箱发送的连接
        cache.set(random_str, email, 120)
        # return HttpResponse("ok")

        return HttpResponse("邮件已发送！！！")
