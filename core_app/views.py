import requests
import requests_cache
from django.shortcuts import render
from django.views import View

requests_cache.install_cache('api_call_cache', backend='sqlite', expire_after=180)
API_TOKEN = 'live_64d523ff143f84a749cc4b6d30bf70'


class Classificacao(View):
    template_name = 'classificacao_brasileirao.html'

    def get(self, request):
        url = 'https://api.api-futebol.com.br/v1/campeonatos/10/tabela'
        headers = {'Authorization': f'Bearer {API_TOKEN}'}
        context = {'data': requests.get(url, headers=headers).json()}

        return render(request, self.template_name, context)


class InformacoesCampeonato(View):
    template_name = 'informacoes_brasileirao.html'

    def get(self, request):
        url = 'https://api.api-futebol.com.br/v1/campeonatos/10'
        headers = {'Authorization': f'Bearer {API_TOKEN}'}
        context = {'data': requests.get(url, headers=headers).json()}

        return render(request, self.template_name, context)
