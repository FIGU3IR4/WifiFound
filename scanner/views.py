from django.shortcuts import render
from django.http import JsonResponse
import nmap

def home(request):
    return render(request, 'scanner/home.html')

def scan_network(request):
    nm = nmap.PortScanner()
    nm.scan(hosts='192.168.0.0/24', arguments='-sn')

    devices = []
    for host in nm.all_hosts():
        devices.append({
            'ip': host,
            'mac': nm[host]['addresses'].get('mac', 'Desconhecido'),
            'hostname': nm[host].hostname() or 'Sem nome'
        })

    return JsonResponse({'devices': devices})
