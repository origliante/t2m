#!/usr/bin/ruby

require 'socket'
require 'yaml'

BUFSIZE = 1024

unless ARGV.count == 2
  puts "Usage: #{$0} listen_ip port_number"
  exit(1)
end

listen_ip = ARGV[0]
port = ARGV[1].to_i

s = UDPSocket.new
s.bind(listen_ip, port)

while true
  mesg, addr = s.recvfrom(BUFSIZE)
  #TODO
  puts mesg
end

