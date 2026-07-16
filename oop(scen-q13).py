class DBSession:

    def __init__(self, host, port, user):
        self.credentials = (host, port, user)


session = DBSession("localhost", 3306, "admin")

print(session.credentials)

try:
    session.credentials[1] = 8080
except TypeError as e:
    print(e)