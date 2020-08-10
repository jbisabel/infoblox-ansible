
import socket
from __future__ import


def validate_ip_address(address):
    try:
        socket.inet_aton(address)
    except socket.error:
        return False
    return address.count('.') == 3


def validate_ip_v6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:
        return False
    return True
