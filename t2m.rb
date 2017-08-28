#!/usr/bin/ruby

require 'socket'
require 'date'
require 'json'
require 'logger'


BUFSIZE = 1024


if test ?d, '/vagrant'
    logfilename = '/vagrant/.t2m.log'
else
    logfilename = '/tmp/.t2m.log'
end
$logger = Logger.new(logfilename)
$logger.level = Logger::DEBUG



unless ARGV.count == 2
  puts "Usage: #{$0} listen_ip port_number"
  exit(1)
end


def s_to_datetime(dts)
    parsed_time = DateTime.strptime(dts, '%d/%m/%Y %H:%M')
    return parsed_time
end


def parse_data(data)
    dtobj = String.new()
    msg = String.new()

    begin
        if data.include? "]"
            dts, msg = data.split(']')
            dts = dts.sub('[', '')
            if msg[0] == ' '
                msg = msg[1..-1]
                dtobj = s_to_datetime(dts)
            end
        end
    ensure
        return dtobj, msg
    end

end


def main()
    listen_ip = ARGV[0]
    port = ARGV[1].to_i

    s = UDPSocket.new
    s.bind(listen_ip, port)

    while true
        mesg, addr = s.recvfrom(BUFSIZE)
        dt, msg = parse_data(mesg)

        if dt != "" and msg != ""
            dict = { "timestamp" => dt.strftime("%s").to_i, "message" => msg }
            print(dict.to_json, "\n")
            $logger.debug("#{dict.to_json}")
            next
        end
        $logger.debug('invalid message received.')
    end
end



main()


