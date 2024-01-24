import subprocess
import platform
import os
import sys
from colorama import init, Fore, Style
init(autoreset=True)
def title():
    if platform.system().lower() == 'Windows':
        os.system(f"title PLAYIT.GG")
    else:
        sys.stdout.write(f"\x1b]2;PLAYIT.GG\x07")
        sys.stdout.flush()
title()

def cls():
    command = 'cls' if platform.system().lower() == 'windows' else 'clear'
    os.system(command)
cls()

def pingprocess(ip):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '2', ip]

    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) == 0

def build_subnet(base_ip, region):
    blocked_ips = []
    for i in range(1, 256):
        ip = f"{base_ip}.{i}"
        if not pingprocess(ip):
            blocked_ips.append(ip)

    if not blocked_ips:
        print(f" {Fore.BLUE}{region}{Style.RESET_ALL}:\n {len(blocked_ips)} ips are {Fore.GREEN}blocked.")
    else:
        print(f" {Fore.BLUE}{region}{Style.RESET_ALL}:\n {len(blocked_ips)} ips are {Fore.RED}blocked.")

    for ip in blocked_ips:
        print(f" [{ip}]: {Fore.RED}Blocked.")

print(f"\n Unofficial {Fore.YELLOW}Playit{Fore.CYAN}.gg{Style.RESET_ALL} IP checker\n")
print(" First checking:\n")

print(f"  {Fore.YELLOW}api{Style.RESET_ALL}.playit.gg: {Fore.GREEN}Ok.{Style.RESET_ALL}" if pingprocess("api.playit.gg") else f"  {Fore.YELLOW}api{Style.RESET_ALL}.playit.gg: {Fore.RED}failed{Style.RESET_ALL}")
print(f"  {Fore.YELLOW}ping{Style.RESET_ALL}.ply.gg: {Fore.GREEN}Ok.{Style.RESET_ALL}" if pingprocess("ping.ply.gg") else f"  {Fore.YELLOW}ping{Style.RESET_ALL}.ply.gg: {Fore.RED}failed{Style.RESET_ALL}")
print(f"  {Fore.YELLOW}Debug{Style.RESET_ALL}.IP: {Fore.GREEN}Ok.{Style.RESET_ALL}" if pingprocess("147.185.221.1") else f"  {Fore.YELLOW}Debug{Style.RESET_ALL}.IP: {Fore.RED}failed{Style.RESET_ALL}")
    
        
print("\n Now working. This will take a while.\n")

subnets = {
    "147.185.221": "GLOBAL",
    "209.25.140": "NORTH AMERICA",
    "209.25.141": "ASIA",
    "209.25.142": "EUROPE",
    "209.25.143": "INDIA",
    "23.133.216": "SOUTH AMERICA"
}

for base_ip, region in subnets.items():
    build_subnet(base_ip, region)
