#!/usr/bin/env python3
import argparse
import nmap


def do_scan(network):
    nm = nmap.PortScanner()
    nm.scan(hosts=network, arguments='-sn')

    devices = []
    for host in nm.all_hosts():
        mac = nm[host]['addresses'].get('mac', 'Desconhecido') \
            if 'addresses' in nm[host] else 'Desconhecido'
        hostname = nm[host].hostname() or 'Sem nome'

        devices.append((host, mac, hostname))

    return devices


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI: Varredura de rede (nmap)')
    parser.add_argument('--network', '-n', default='192.168.0.0/24')
    args = parser.parse_args()

    devices = do_scan(args.network)

    if devices:
        print(f"\nDispositivos encontrados na rede {args.network}:")
        print("-" * 50)
        for ip, mac, hn in devices:
            print(f"- IP: {ip} | MAC: {mac} | HOSTNAME: {hn}")
    else:
        print("\nNenhum dispositivo encontrado.")
