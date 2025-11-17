from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home'),
# rota que retorna JSON (para testes e API)
path('scan/', views.scan_network_json, name='scan_network'),
# rota que retorna HTML (interface)
path('scan-html/', views.scan_network_html, name='scan_network_html'),
]