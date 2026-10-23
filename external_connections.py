import socket

class ExternalConnections:
    """Class that deals with external_connections

    Establishes the port that listens to external connections and connects to them.
    Facilitates two way communcation

    Attributes:
        host: local machine's ip address
        port: Port being listened to
        socket: Facilitates communication
        conn: The socket's connection
        addr: The client's ip address
    """

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(1)
        print(f'Listening on host {host} and port {port}')
        self.conn, self.addr = self.sock.accept()
        print(f'Connection with {self.addr} successfully established')


    def __del__(self):
        self.sock.close()


    def recieveData(self, bufsize=1024):
        """Gets and returns data from connection"""
        while True:
            packet = self.sock.recv(bufsize)
            if not packet:
                return None
            return packet


    def sendData(self, data):
        """Sends data to client"""
        self.sock.sendall(data)
        print("Data has been sent")