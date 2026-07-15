#Aik Server class banayein jahan class level par
# provider_name = "AWS" ho aur instance level par
#server ki ip_address ho. Explain karein ke humne provider name ko class level par kyun rakha.
class Server:
    provider_name = "AWS"      # Class Attribute

    def __init__(self, ip_address):
        self.ip_address = ip_address   # Instance Attribute

server1 = Server("192.168.1.10")
server2 = Server("10.0.0.5")

print(Server.provider_name)
print(server1.ip_address)
print(server2.ip_address)