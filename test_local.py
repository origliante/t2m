import os
import time
import subprocess

import unittest
import test

class LocalTestCase(test.VagrantTestCase):
    """Local tests for `t2m.py`."""
    T2M_IP = '127.0.0.1'
    T2M_PORT = 1999
    python_proc = None

    def setUp(self):
        #os.system("rm -f /tmp/.t2m.log")
        #proc = subprocess.Popen(['python', 't2m.py', '0.0.0.0', '1999'])
        #'%s' % self.T2M_IP, '%s' % self.T2M_PORT], shell=True)
        #self.python_proc = proc
        pass

    def tearDown(self):
        if self.python_proc:
            self.python_proc.terminate()

    def get_logdata(self):
        time.sleep(2)
        lastline = ''
        with file('/tmp/.t2m.log', 'r') as f:
            for line in f:
                lastline = line
        print lastline
        return lastline


if __name__ == '__main__':
    unittest.main()


