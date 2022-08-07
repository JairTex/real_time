from django.urls import re_path #Path com expressões regulares
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<nome_sala>\w+)/$', ChatConsumer), # r'str' indica que dentro '\' não é caracter de escape
]
