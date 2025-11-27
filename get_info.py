from netmiko import ConnectHandler
import getpass

password = getpass.getpass("Input password for SSH: ")

devices = {
    'device_type': 'cisco_ios',
    'host': '10.100.255.7',
    'username': '3pshrespa',
    'password': password,
    'disabled_algorithms': {
            "pubkeys": ["rsa-sha2-256", "rsa-sha2-512"]}
    
    }

net_connect = ConnectHandler(**devices)
net_connect.enable()
#command_output_1 = net_connect.send_command("show running | inc hostname", read_timeout = 30, use_textfsm = True)
command_output_2 = net_connect.send_command("show ip int br | ex unas ", read_timeout = 30, use_textfsm = True)
command_output_3 = net_connect.send_command("show version ", read_timeout = 30, use_textfsm = True)
net_connect.disconnect()

#print(command_output_3)

for info in command_output_3:
    software_image = info["software_image"]
    software_version = info["version"]
    hostname = info["hostname"]
    hardware = info["hardware"]
    mac_addr = info["mac_address"]
    serial = info["serial"]
    print(f"HOSTNAME : {hostname} \n    software: {software_version} \n    hardware: {hardware} \n    MAC: {mac_addr} \n    Serial: {serial} ")
          


# print("--------------------------------------------------------")
# print(command_output_1)
print()
print("    IP ADDRESS INFO")

for ips in command_output_2:
    interface = ips["interface"]
    ipaddr = ips["ip_address"]

    print(f"      {interface}:{ipaddr}")

print("--------------------------------------------------------")





