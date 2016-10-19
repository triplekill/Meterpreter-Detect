#!/usr/bin/env python
# checks to see if a port is running a metasploit reverse https listener service.
# checks a url for the existence of a file called "chpwd.htm" which contains "core_patch_url" in its contents.
# context: http://x42.obscurechannel.com/?p=197
# author: @0rbz_ (Fabrizio Siciliano)
# usage: python meterpreter-detect.py http(s)://ip:port

import os
import sys

class x:
    r = '\033[91m'
    b = '\033[0m'

if len(sys.argv) != 2:
    print 'Usage: python %s [http(s)://ip:port]' % sys.argv[0]
    exit()

target_ip = sys.argv[1]
finger = os.system("wget -qO- --no-check-certificate " + target_ip + "/chpwd.htm" + " --output-document=/tmp/handler_finger")

with open('/tmp/handler_finger', 'r') as content:
    content = content.read()

if "core_patch_url" in content:
    print x.r + "*** Looks like a Metasploit Handler is listening on " + target_ip + " ***" + x.b

if "core_patch_url" not in content:

    print x.r + "Not a Metasploit Listener."
