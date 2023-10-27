#!/use/bin/env python
import subprocess
import argparse
import re

interface = input("Interface > ")
new_mac = input("New MAC > ")

print(f"[+] Changing MAC Address of {interface} to {new_mac}")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

# If wlan0 is missing
# google: https://mirror2.openwrt.org/sources/
# download compat-wireless-2010-06-28.tar.bz2
# tar -jxvf compat-wireless-2010-06-28.tar.bz2      - extract
# cd compat-wireless-2010-06-28
# sudo make unload
# sudo make load
# ifconfig