#! /usr/bin/env python
# Requires python 2.7

import sys
import socket
import datetime
import json
import logging

import os

if os.path.exists('/vagrant'):
    logfilename = '/vagrant/.t2m.log'
else:
    logfilename = '/tmp/.t2m.log'

logging.basicConfig(
    filename=logfilename,
    level=logging.DEBUG)


BUFSIZE = 1024
DEBUG = True


def main():
    if len(sys.argv) < 2:
        usage()
    try:
        server()
    except Exception, e:
        logging.critical("server() exited with exception %s" % str(e))

def usage():
    sys.stdout = sys.stderr
    print('Usage: %s listen_ip udp_port' % sys.argv[0])
    sys.exit(2)


def debug(msg):
    if DEBUG: logging.debug(msg)


def s_to_datetime(dts):
    try:
        dtobj = datetime.datetime.strptime(dts, "%d/%m/%Y %H:%M")
        return dtobj
    except ValueError:
        return False

def parse_data(data):
    """
    Quick n dirty data parsing.
    string -> datetime, string
    """
    dtobj = None
    msg = None
    if ']' not in data:
        return dtobj, msg
    try:
        dts, msg = data.split(']')
        dts = dts.strip('[')
        if msg[0] != ' ':
            return dtobj, msg
        msg = msg[1:]
        dtobj = s_to_datetime(dts)
    except ValueError:
        pass
    return dtobj, msg


def server():
    if len(sys.argv) > 2:
        host = sys.argv[1]
        port = eval(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    debug('udp server ready on %s:%s' % (host,port))
    while 1:
        data, addr = s.recvfrom(BUFSIZE)
        debug('server received %r from %r' % (data, addr))

        dt, msg = parse_data(data)
        if dt and msg:
            #send data back
            datadict = {
                "timestamp": (dt - datetime.datetime(1970,1,1)).total_seconds(),
                "message": msg
            }
            jsondata = json.dumps(datadict)
            debug(jsondata)
            print(jsondata)
            s.sendto(jsondata, addr)
        else:
            debug('invalid message received.')


if __name__ == '__main__': main()


