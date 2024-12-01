from sys import platform
import subprocess, os


def linux_get_networks():
    network_connections = []
    for filename in os.listdir("/etc/NetworkManager/system-connections/"):
        network_connections.append(filename.split(".")[0])
    return network_connections

def lp(ssid):
    exec = subprocess.run(['nmcli', 'con' , "up", ssid], capture_output=True, text=True).stdout
    print(f"Connected to {ssid}")
    enum()

def enum():
    exec = subprocess.run(['for ip in {1..254..1};do ping -c 1 192.168.1.$ip | grep "64 b" | cut -d " " -f 4 >> out.txt; done'], capture_output=True, text=True).stdout
    print(exec)

def connect_back(ssid):
    exec = subprocess.run(['nmcli', 'con' , "up", ssid], capture_output=True, text=True).stdout
    print("Connected to orginal connection")

def main():
    if (platform == "linux"):
        og_ssid = subprocess.run(['iwgetid', '-r'], capture_output=True, text=True).stdout
        for network in linux_get_networks():
            lp(network)
        connect_back(og_ssid)
main()
