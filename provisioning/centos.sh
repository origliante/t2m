#!/bin/bash

yum -y install psmisc
yum -y install python
yum -y update python

# fix for the private network interface coming up with a different
# address until network restart 
systemctl stop network
systemctl start network

