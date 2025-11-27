This program loops through several IP addresses present on the device_list.txt file.
It then collects important info using netmiko and textfsm : software_version, hardware, hostname, serial number and MAC addresses & all assigned IP addresses on the device.

The output is saved in separate file for each host. The filename is saved as the {hostname}_device_info.txt in another directory.
