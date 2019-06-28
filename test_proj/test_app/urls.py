from django.conf.urls import url, include
from test_app import views


urlpatterns = [
    # url('', views.index, name='index'),
    url('index', views.index, name='index'),
    url('base', views.base, name='base'),
    url(r'(?P<regions>.*)', views.region, name='region'),
    # url('', views.index, name='index'),
]