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

    T2M_IP = '192.168.42.42'
    T2M_PORT = 1999

    def setUp(self):
        os.system("rm -f .t2m.log")
        os.system("vagrant provision")

    def get_logdata(self):
        logdata = file('.t2m.log', 'r').read()
        return logdata

    def test_invalid_msg(self):
        client(self.T2M_IP, self.T2M_PORT, 'test')
        #FIXME: how to force a log flush?
        time.sleep(2)
        logdata = self.get_logdata()
        #print(logdata)
        self.assertTrue("server received 'test' from" in logdata)
        self.assertTrue("invalid message received." in logdata)

    def test_proper_msg(self):
        client(self.T2M_IP, self.T2M_PORT, '[3/6/2007 12:12] Hello World!')
        logdata = self.get_logdata()
        #print(logdata)
        self.assertTrue("" in logdata)


if __name__ == '__main__':
    unittest.main()


