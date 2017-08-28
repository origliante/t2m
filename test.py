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
        #os.system("rm -f .t2m.log")
        #os.system("vagrant provision")
        pass

    def get_logdata(self):
        time.sleep(2)
        lastline = ''
        with file('.t2m.log', 'r') as f:
            for line in f:
                lastline = line
        print lastline
        return lastline

    def do_test_invalid_msg(self, msg):
        client(self.T2M_IP, self.T2M_PORT, msg)
        #FIXME: how to force a log flush?
        time.sleep(2)
        logdata = self.get_logdata()
        #print(logdata)
        self.assertTrue("invalid message received." in logdata)

    def test_invalid_msg_1(self):
        self.do_test_invalid_msg('test')

    def test_invalid_msg_2(self):
        self.do_test_invalid_msg('[3/6/2007 12:13] ')

    def test_invalid_msg_3(self):
        self.do_test_invalid_msg('[3/6/2007 12:13]')

    def test_invalid_msg_4(self):
        self.do_test_invalid_msg('[3/6-2007 12:13]')

    def test_invalid_msg_5(self):
        self.do_test_invalid_msg('3/6/2007 12:13]')

    def test_proper_msg(self):
        import random
        randint = random.randint(0, 9999)
        client(self.T2M_IP, self.T2M_PORT, '[3/6/2007 12:12] Hello World %s' % randint)
        logdata = self.get_logdata()
        #print(logdata)
        msgs = [
            #python
            '{"timestamp": 1180872720, "message": "Hello World %s"}' % randint,
            #ruby
            '{"timestamp":1180872720,"message":"Hello World %s"}' % randint
        ]
        print 'logdata ', logdata
        self.assertTrue(msgs[0] in logdata or msgs[1] in logdata)


if __name__ == '__main__':
    unittest.main()


