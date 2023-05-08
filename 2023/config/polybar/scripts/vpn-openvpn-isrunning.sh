#!/bin/sh
country=$(protonvpn s | grep Country)
connection=$(pgrep -a openvpn$ | head -n 1 | awk '{print $NF }' | cut -d '.' -f 1)

if [ -n "$connection" ]; then
    echo "vpn  on" $country
else 
    echo "vpn  off"
fi