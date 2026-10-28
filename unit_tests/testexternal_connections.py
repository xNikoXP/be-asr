import struct

from unittest import main
from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch

from main.external_connections import ExternalConnections as EC

class TestExternalConnections(TestCase):
    
    def test_receive(self):
        with patch.object(EC, "__init__", return_value=None):
            ec = EC()
        message = b'This is a test'
        length = struct.pack('>I', len(message))
        packet = length + message;
        ec.sock = Mock()
        ec.sock.recv.return_value = packet
        assert ec.receive() == packet

    def test_receive_null(self):
        with patch.object(EC, "__init__", return_value=None):
            ec = EC()
        ec.sock = Mock()
        ec.sock.recv.return_value = None
        assert ec.receive() == None

if __name__ == '__main__':
    main