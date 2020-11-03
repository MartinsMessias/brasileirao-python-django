"""brasileirao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core_app.views import Classificacao, InformacoesCampeonato, Rodadas, Rodada, Artilharia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classificacao/', Classificacao.as_view(), name='classificacao'),
    path('informacoes/', InformacoesCampeonato.as_view(), name='info_campeonato'),
    path('rodadas/', Rodadas.as_view(), name='rodadas'),
    path('rodada/<str:rodada>', Rodada.as_view(), name='rodada'),
    path('artilheiros/', Artilharia.as_view(), name='artilheiros'),
]
