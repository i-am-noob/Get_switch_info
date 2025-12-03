from netmiko import ConnectHandler
import getpass
from datetime import datetime






def get_credentials():
    
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    return username, password



def get_device_ip(file_path):
    
    with open(file_path, "r") as f:
         ip = [ ips.strip() for ips in f if ips.strip()]

    return ip
    


def create_device(ip_host, username, password):
        
        devices = {
            'device_type': 'cisco_ios',
            'host': ip_host,
            'username': username,
            'password': password,
            'disabled_algorithms': {
                    "pubkeys": ["rsa-sha2-256", "rsa-sha2-512"]}
            
            }
        return devices



def collect_data(net_connect):
                        
        ip_info = net_connect.send_command("show ip int br | ex unas ", read_timeout = 30, use_textfsm = True)
        version_info = net_connect.send_command("show version ", read_timeout = 30, use_textfsm = True)
        print(version_info)
        #net_connect.disconnect()
        return ip_info, version_info

def format_data(version_info, ip_info):
        
                
        output_lines = []

        #print(version_info)

        for info in version_info:
            #software_image = info["software_image"]
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

        return final_output, hostname

        #file_name = f"{hostname}_device_info.txt"

def write_output_file(text, hostname):
            
            dir_path = "/home/spandan/Desktop/Python_Practice/Output"

            timestamp = datetime.now().strftime("%Y%m%d_%H%M")

            file_path = f"{dir_path}/{hostname}_{timestamp}_device_info.txt"     
            
            with open(file_path, "w") as f:
                  f.write(text)
                                
                                

def main():
     username,password = get_credentials()
     ip_list = get_device_ip("/home/spandan/Desktop/Python_Practice/file.txt")

     for ip in ip_list:
            
            device = create_device(ip, username, password)
            net_connect = ConnectHandler(**device)
            net_connect.enable()

            ip_info, version_info = collect_data(net_connect)
            net_connect.disconnect()

            final_text, hostname = format_data(version_info, ip_info)
            write_output_file(final_text, hostname)

if __name__ == "__main__":
       main()













