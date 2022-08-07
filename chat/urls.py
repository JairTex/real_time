from django.urls import path
from .views import IndexView, SalaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('chat/<str:nome_sala>/', SalaView.as_view(), name='sala'), #Para cada sala ter sua url própria
]