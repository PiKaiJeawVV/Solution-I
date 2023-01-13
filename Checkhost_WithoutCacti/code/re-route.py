from netmiko import ConnectHandler
import re
import mysql.connector
# .send_config_set = สั่งให้ Config หรือมีการเปลี่ยนแปลง
# .send_command = สั่งให้ show command

db_nms2 = mysql.connector.connect(host="192.168.71.29",user="admin",password="htvnms",database="htv",port=3306)
insert_db = db_nms2.cursor()
#ii = ['10.0.0.50','10.0.0.51','10.0.0.52','10.0.0.53','10.0.0.54','10.0.0.55']

regex = r"!!!!!"

net_connect = ConnectHandler(device_type="cisco_ios_telnet",host="10.0.0.53",username="program",password="Htv027306921",)

insert_db.execute(f"select * from PonFixIpList where Oltip = '172.21.3.1' and cus_id != ' ';")
Oltip_list = []
FixIp_list = []

for i in insert_db:
    get_oltip = i[1]
    get_fixip = i[2]
    Oltip_list.append(get_oltip)
    FixIp_list.append(get_fixip)

for oo,ii in zip(Oltip_list,FixIp_list):
    print(oo,ii)
    try:
        show_route = net_connect.send_command(f"ping {ii}", use_textfsm=True, read_timeout=2)
        print("Can find IP")
        check = re.search(regex, show_route)
        if check:
            values = 1
            print(values)
            print(ii)
        else:
            values = 2
            print(values)
            print(ii)
    except:
        pass
        values = 2
        print("Can't find IP")
        print(values)

db_nms2.close()