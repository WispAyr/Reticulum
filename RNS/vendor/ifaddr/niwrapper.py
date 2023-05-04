# netifaces compatibility layer

import ifaddr
import socket

from typing import List

AF_INET6 = socket.AF_INET6.value
AF_INET = socket.AF_INET.value

def interfaces() -> List[str]:
    adapters = ifaddr.get_adapters(include_unconfigured=True)
    return [a.name for a in adapters]

def ifaddresses(ifname) -> dict:
    adapters = ifaddr.get_adapters(include_unconfigured=True)
    ifa = {}
    for a in adapters:
        if a.name == ifname:
            ipv4s = []
            ipv6s = []
            for ip in a.ips:
                t = {}
                if ip.is_IPv4:
                    t["addr"] = ip.ip
                    ipv4s.append(t)
                if ip.is_IPv6:
                    t["addr"] = ip.ip[0]
                    ipv6s.append(t)

            if len(ipv4s) > 0:
                ifa[AF_INET] = ipv4s
            if len(ipv6s) > 0:
                ifa[AF_INET6] = ipv6s

    return ifa