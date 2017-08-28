import os
import time

import unittest
import test

class DockerTestCase(test.VagrantTestCase):
    """Docker tests for `t2m.py`."""
    T2M_IP = '127.0.0.1'
    T2M_PORT = 1999

    def setUp(self):
        os.system("docker kill t2m_test; docker rm t2m_test")
        os.system("docker run --name t2m_test -d -t -p 1999:1999/udp test/python:centos7")
        #os.system("rm -f .t2m.log")

    def get_logdata(self):
        time.sleep(2)
        os.system("docker cp t2m_test:/tmp/.t2m.log .t2m.log")
        lastline = ''
        with file('.t2m.log', 'r') as f:
            for line in f:
                lastline = line
        print lastline
        return lastline
 

if __name__ == '__main__':
    unittest.main()

