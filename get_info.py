from netmiko import ConnectHandler
import getpass

username = input("Username: ")
password = getpass.getpass("Password: ")

with open("device_list.txt", "r") as f:
    
    for ip_address in f:
        ip_host = ip_address.strip()

        devices = {
            'device_type': 'cisco_ios',
            'host': ip_host,
            'username': username,
            'password': password,
            'disabled_algorithms': {
                    "pubkeys": ["rsa-sha2-256", "rsa-sha2-512"]}
            
            }

        net_connect = ConnectHandler(**devices)
        net_connect.enable()

        ip_info = net_connect.send_command("show ip int br | ex unas ", read_timeout = 30, use_textfsm = True)
        version_info = net_connect.send_command("show version ", read_timeout = 30, use_textfsm = True)
        net_connect.disconnect()

        output_lines = []

        #print(version_info)

        for info in version_info:
            software_image = info["software_image"]
            software_version = info["version"]
            hostname = info["hostname"]
            hardware = ", ".join(info["hardware"])
            mac_addr = ", ".join(info["mac_address"])
            serial = ", ".join(info["serial"])
            output_lines.append(f"HOSTNAME : {hostname} \n    software: {software_version} \n    hardware: {hardware} \n    MAC: {mac_addr} \n    Serial: {serial} ")
                
        
        output_lines.append("\n    IP ADDRESS INFO")

        for ips in ip_info:
            interface = ips["interface"]
            ipaddr = ips["ip_address"]

            output_lines.append(f"      {interface}:{ipaddr}")

        output_lines.append("--------------------------------------------------------")

        final_output = f"\n".join(output_lines)

        file_name = f"{hostname}_device_info.txt"

        with open(f"/home/spandan/Desktop/Automation/switch_info/{file_name}", "w") as f:
            f.write(final_output)







