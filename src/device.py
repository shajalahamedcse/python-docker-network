from netmiko import ConnectHandler

#config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
#output = net_connect.send_config_set(config_commands)
#print(output)

class Device:
    
    data = []
    db = {}

    def __init__(self, params):
        self.params = params

    def gather_info(self):
        for i in self.params:
            net_connect = ConnectHandler(**i)
            output = net_connect.send_command('ip a')
            #print(output)
            self.data.append(output.split())

        for j in range(len(self.data)):
            k = str(self.data[j][27]).replace(':', '')
            v = str(self.data[j][44])
            z = v[:v.find('/')]
            self.db[z] = k
        
        return self.db

    
    def show_info(self):
        if self.data:
            return self.data
        else:
            print("No data found !")



