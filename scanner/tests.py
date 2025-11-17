from django.test import TestCase, Client
from django.urls import reverse
import json


class ScanNetworkTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_scan_route_returns_json(self):
        """
        Testa se a rota principal /scan retorna JSON corretamente.
        """
        response = self.client.get(reverse('scan_network'))

        # Verifica que a resposta retorna OK
        self.assertEqual(response.status_code, 200)

        # Garantir tipo JSON
        self.assertEqual(response['Content-Type'], 'application/json')

        # Converter e validar estrutura
        data = json.loads(response.content)
        self.assertIn('devices', data)

    def test_scan_route_handles_invalid_network(self):
        """
        Testa se a rota lida com redes inválidas (ex: ?network=invalid_network).
        Podemos aceitar 200 (tratado) ou 500 (erro interno capturado).
        O importante é garantir que ainda retorna JSON.
        """
        response = self.client.get(reverse('scan_network') + '?network=invalid_network')

        # Aceita tanto 200 quanto 500 dependendo de como a view trata o erro
        self.assertIn(response.status_code, (200, 500))

        # Deve retornar JSON mesmo em erro
        self.assertEqual(response['Content-Type'], 'application/json')
