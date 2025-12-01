'''Write a read_device_list(file_path) to read IPs from a file and return as a list'''

def read_device_list(file_path):
    ip = []
    with open(file_path, "r") as f:
        for ips in f:
            cleaned = ips.strip()
            if cleaned:
                ip.append(cleaned)
            
            
    return ip
        
def main():
    ip = read_device_list("/home/spandan/Desktop/Python_Practice/file.txt")
    print(ip)

if __name__ == "__main__":
    main()
