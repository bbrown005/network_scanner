#!/usr/bin.env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
# end scan


scan("10.0.2.1/24")
# Use ARP to ask for IP



# Set destination MAC to broadcast MAC
