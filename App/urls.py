from django.conf.urls import url

from .views import email, yemian, zhuce, jihuo

urlpatterns = [

    url(r'^email/',email),
    url(r'^yemian/',yemian),
    url(r'^zhuce/',zhuce),
    url(r'^jihuo/(.+)',jihuo)
]
