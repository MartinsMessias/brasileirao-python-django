import requests
import requests_cache
from django.shortcuts import render
from django.views import View

requests_cache.install_cache('api_call_cache', backend='sqlite', expire_after=180)
API_TOKEN = 'test_507a1b98973ec201a987732daf6241'


class Home(View):
    template_name = 'index.html'

    def get(self, request):
        url = 'https://api.api-futebol.com.br/v1/campeonatos'
        headers = {'Authorization': f'Bearer {API_TOKEN}'}
        context = {'data': requests.get(url, headers=headers).json()}

        return render(request, self.template_name, context)
