import subprocess
import platform
import os
import sys
from colorama import init, Fore, Style
import time
import webbrowser
import socket


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

def automatic_mode():
    # Placeholder for Automatic mode functionality
    print("Automatic mode is not yet implemented.")
    
def bruteforce_mode():
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


def manual_mode():
    print(f" You need to paste your {Fore.CYAN}tunnel address{Style.RESET_ALL} here. {Fore.YELLOW}Don't know where to find it?{Style.RESET_ALL} Type: {Fore.CYAN}idk{Style.RESET_ALL}")
    while True:
        try:
            ip = input(f" Please enter your tunnel {Fore.CYAN}address{Fore.YELLOW}/{Fore.BLUE}ipv4{Style.RESET_ALL}: ")
            if (ip.lower())=="idk":
                webbrowser.open("https://i.imgur.com/kTeKsRO.png", new=2)
            address = ip.split(':')[0]
            if not pingprocess("ping.ply.gg"):
                try:
                    if not address.replace('.', '').isdigit():
                        address = socket.gethostbyname(address)
                except socket.gaierror:
                    print(f" {Style.RESET_ALL}[{Fore.RED}ERROR.{Style.RESET_ALL}] Please use the IPV4.")
            else:
                if pingprocess(address):
                    print(f" [{address}]: {Fore.GREEN}OK.")
                else:
                    print(f" [{address}]: {Fore.RED}Blocked.")
                break
        except ValueError:
            print(f" Wrong Input.")


def get_user_mode():
    print(f"\n Select the mode you want to use:")
    print(f" [{Fore.YELLOW}1{Style.RESET_ALL}] Automatic  [{Fore.YELLOW}2{Style.RESET_ALL}] Bruteforce  [{Fore.YELLOW}3{Style.RESET_ALL}] Manual")

    while True:
        try:
            choice = int(input(f" >"))
            if choice in [1, 2, 3]:
                return choice
            else:
                print(f" Invalid choice.")
                time.sleep(1)
        except ValueError:
            print(f" Please enter a number.")
            
if __name__ == "__main__":
    title()
    cls()

    print(f"\n Unofficial {Fore.YELLOW}Playit{Fore.CYAN}.gg{Style.RESET_ALL} IP checker\n")
    print(" First checking:\n")

    print(f"  {Fore.YELLOW}api{Style.RESET_ALL}.playit.gg: {Fore.GREEN}Ok.{Style.RESET_ALL}" if pingprocess("api.playit.gg") else f"  {Fore.YELLOW}api{Style.RESET_ALL}.playit.gg: {Fore.RED}failed{Style.RESET_ALL}")
    print(f"  {Fore.YELLOW}ping{Style.RESET_ALL}.ply.gg: {Fore.GREEN}Ok.{Style.RESET_ALL}" if pingprocess("ping.ply.gg") else f"  {Fore.YELLOW}ping{Style.RESET_ALL}.ply.gg: {Fore.RED}failed{Style.RESET_ALL}")
    print(f"  {Fore.YELLOW}Debug{Style.RESET_ALL}.IP: {Fore.GREEN}Ok.{Style.RESET_ALL}" if pingprocess("147.185.221.1") else f"  {Fore.YELLOW}Debug{Style.RESET_ALL}.IP: {Fore.RED}failed{Style.RESET_ALL}")

    user_mode = get_user_mode()

    if user_mode == 1:
        automatic_mode()
    elif user_mode == 2:
        bruteforce_mode()
    elif user_mode == 3:
        manual_mode()
