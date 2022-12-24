from netmiko import ConnectHandler

# .send_config_set = สั่งให้ Config หรือมีการเปลี่ยนแปลง
# .send_command = สั่งให้ show command
net_connect = ConnectHandler(device_type="cisco_ios_telnet",host="10.0.0.60",username="program",password="1qaz2wsx",)

show_route = net_connect.send_command("show ip route static | include 0.0.0.0/0")
#command_config = ['no ip route 0.0.0.0 0.0.0.0 192.168.50.254','ip route 0.0.0.0 0.0.0.0 10.0.0.254']

#output = net_connect.send_command(command)
#output = net_connect.send_config_set(command_config)
show_len = len(show_route)

print(show_len)
print(show_route)
print(show_route.split()[4])
#output_.split()