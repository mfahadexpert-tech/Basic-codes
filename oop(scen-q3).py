class CloudServer:

    __active_servers_count = 0

    def __init__(self):
        CloudServer.__active_servers_count += 1
        self.server_id = f"Server-{100 + CloudServer.__active_servers_count}"

    @classmethod
    def get_active_servers(self):
        return self.__active_servers_count


s1 = CloudServer()
s2 = CloudServer()
s3 = CloudServer()

print(s1.server_id)
print(s2.server_id)
print(s3.server_id)

print("Active Servers:", CloudServer.get_active_servers())