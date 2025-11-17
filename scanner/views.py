from django.shortcuts import render
from django.http import JsonResponse
import nmap


def home(request):
    return render(request, 'scanner/home.html')


def _do_scan(network_param):
    """
    Função interna que executa o nmap e retorna a lista de dispositivos.
    Retorna lista de dicts com chaves: ip, mac, hostname
    """
    nm = nmap.PortScanner()
    nm.scan(hosts=network_param, arguments='-sn')

    devices = []
    for host in nm.all_hosts():
        mac = nm[host]['addresses'].get('mac', 'Desconhecido') if 'addresses' in nm[host] else 'Desconhecido'
        hostname = nm[host].hostname() or 'Sem nome'

        devices.append({
            'ip': host,
            'mac': mac,
            'hostname': hostname
        })

    return devices


def scan_network_json(request):
    network_param = request.GET.get('network', '192.168.0.0/24')
    try:
        devices = _do_scan(network_param)
        return JsonResponse({
            'devices': devices,
            'network_scanned': network_param
        })
    except Exception as e:
        return JsonResponse({
            'devices': [],
            'network_scanned': network_param,
            'error': str(e)
        }, status=500)


def scan_network_html(request):
    network_param = request.GET.get('network', '192.168.0.0/24')

    try:
        devices = _do_scan(network_param)
        error = None
    except Exception as e:
        devices = []
        error = str(e)

    return render(request, 'scanner/result.html', {
        'devices': devices,
        'network_scanned': network_param,
        'error': error
    })
