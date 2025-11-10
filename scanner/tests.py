from django.test import TestCase, Client
from django.urls import reverse
import json

class ScanNetworkTests(TestCase):
    def setUp(self):
        # Cria um cliente de teste do Django
        self.client = Client()

    def test_scan_route_returns_json(self):
        """
        Testa se a rota /scan/ retorna um JSON válido com a chave 'devices'
        """
        # Faz uma requisição GET para a rota /scan/
        response = self.client.get(reverse('scan_network'))

        # Verifica se a resposta é 200 OK
        self.assertEqual(response.status_code, 200)

        # Verifica se o tipo de conteúdo é JSON
        self.assertEqual(response['Content-Type'], 'application/json')

        # Converte o conteúdo em dicionário Python
        data = json.loads(response.content)

        # Verifica se existe a chave 'devices'
        self.assertIn('devices', data)
