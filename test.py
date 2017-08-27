import unittest
import socket
import os
import time

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
    sock.sendto(message, (ip, port))



class VagrantTestCase(unittest.TestCase):
    """Vagrant tests for `t2m.py`."""
    def setUp(self):
        os.system("rm -f .t2m.log")
        os.system("vagrant provision")
        pass

    def test_invalid_msg(self):
        client('192.168.42.42', 1999, 'test')
        #FIXME: how to force a log flush?
        time.sleep(2)
        logdata = file('.t2m.log', 'r').read()
        #print(logdata)
        self.assertTrue("server received 'test' from" in logdata)
        self.assertTrue("invalid message received." in logdata)

    def test_proper_msg(self):
        client('192.168.42.42', 1999, '[3/6/2007 12:12] Hello World!')
        logdata = file('.t2m.log', 'r').read()
        #print(logdata)
        self.assertTrue("" in logdata)



if __name__ == '__main__':
    unittest.main()

