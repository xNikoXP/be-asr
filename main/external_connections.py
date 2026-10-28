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

    def __init__(self, mac_addr):
        self.sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, proto=socket.BTPROTO_SCO)
        self.sock.bind(mac_addr)
        self.sock.listen(1)
        print(f'Listening on mac address {mac_addr}')
        self.conn, self.addr = self.sock.accept()
        print(f'Connection with {self.addr} successfully established')


    def __del__(self):
        self.sock.close()


    def receive(self, bufsize=1024):
        """Gets and returns data from connection"""
        packet = self.sock.recv(bufsize)
        if not packet:
            return None
        return packet


    def send(self, data):
        """Sends data to client"""
        self.sock.sendall(data)
        print("Data has been sent")