# local

from anansinet.models.Host import Host

# pip
import netaddr
from netaddr.ip import IPAddress

import netifaces
from netifaces.defs import Addresses, InterfaceType, DefaultGatewayEntry, Address

# ? importing classes with full path because ruff can't detect nested names
from scapy.all import srp  # Using srp instead of sr1 for batch processing
from scapy.layers.l2 import ARP, Ether 
from scapy.packet import Packet
from scapy.plist import SndRcvList


def get_default_interface() -> str:
    """
    Returns the default IPv4 interface
    """
    gateways: DefaultGatewayEntry = netifaces.default_gateway()
    if len(gateways) > 0 and len(gateways[netifaces.AF_INET]) > 0:
        return gateways[InterfaceType.AF_INET][1]
    
    raise Exception("counldn't get default interface")


def get_default_gateway() -> str:
    """
    Returns the default IPv4 gateway address
    """
    gateways: DefaultGatewayEntry = netifaces.default_gateway()
    if len(gateways) > 0 and len(gateways[netifaces.AF_INET]) > 0:
        return gateways[netifaces.AF_INET][0]
    
    raise Exception("counldn't get default gateway")


def get_default_netmask(interface: str) -> Address:
    """
    Returns the default IPv4 netmask associated to an interface
    """
    ifaddrs: Addresses = netifaces.ifaddresses(interface)
    
    if netifaces.AF_INET in ifaddrs:
        mask: Address | None = ifaddrs[InterfaceType.AF_INET][0].get("mask")
        if mask is not None:
            return mask
    
    raise Exception("counldn't get default network mask")


gateway_ip: str = get_default_gateway()
interface: str = get_default_interface()
netmask: str = get_default_netmask(interface)
iprange: list[IPAddress] = list[IPAddress](netaddr.IPNetwork('{}/{}'.format(gateway_ip, netmask)))

max_workers = 8       # Increased max threads (2× your logical core count)
retries = 0            # Small retry value to improve speed
timeout = 3            # Timeout
batch_size = 75        # Batch size for ARP requests
resolve_timeout = 1.0


def _sweep_batch(ips: list[IPAddress]) -> list[Host]:
    """
    Sends ARP packets in batch and processes responses
    """
    if not ips:
        return []

    # Create Ethernet frame with ARP request for each IP
    arp_requests: list[Packet] = [Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=str(ip)) for ip in ips]
    
    # Send all requests at once and collect responses
    responses: SndRcvList
    responses, _ = srp(arp_requests, timeout=timeout, retry=retries,
                        verbose=0, iface=interface)

    # Process responses
    hosts: list[Host] = []
    for _, received in responses:
        hosts.append(Host(received.psrc, received.hwsrc))  # pyright: ignore[reportAny]
    return hosts

def scan_connected_hosts() -> list[Host]:
    # Split IP addresses into batches
    ip_batches: list[list[IPAddress]] = [iprange[i:i + batch_size] for i in range(0, len(iprange), batch_size)]
    hosts:list[Host] = []

    for batch in ip_batches:
        batch_hosts: list[Host] = _sweep_batch(batch)
        if batch_hosts:
            hosts.extend(batch_hosts)

    return hosts
    # for host in hosts:
    #     print(f"{host.name}: {host.ip}")

# _ = scan(iprange)