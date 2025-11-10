from django.shortcuts import render
import nmap

def home(request):
    return render(request, 'scanner/home.html')

def scan_network(request):
    nm = nmap.PortScanner()
    network_param = request.GET.get('network', '192.168.0.0/24')
    nm.scan(hosts=network_param, arguments='-sn')

    devices = []
    for host in nm.all_hosts():
        devices.append({
            'ip': host,
            'mac': nm[host]['addresses'].get('mac', 'Desconhecido'),
            'hostname': nm[host].hostname() or 'Sem nome'
        })

    return render(request, 'scanner/result.html', {
        'devices': devices,
        'network_scanned': network_param
    })
