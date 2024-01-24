import subprocess
import platform

def pingprocess(ip):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', ip]

    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) == 0

def build_subnet(base_ip, region):
    blocked_ips = []
    for i in range(1, 256):
        ip = f"{base_ip}.{i}"
        if not pingprocess(ip):
            blocked_ips.append(ip)

    print(f"{region}:\n{len(blocked_ips)} ips are blocked.")
    for ip in blocked_ips:
        print(f"[{ip}]: Blocked.")

subnets = {
    "147.185.221": "GLOBAL",
    "209.25.140": "AMERICA",
    "209.25.141": "ASIA",
    "209.25.142": "EUROPE",
    "209.25.143": "INDIA",
    "23.133.216": "SOUTH AFRICA"
}

for base_ip, region in subnets.items():
    build_subnet(base_ip, region)
