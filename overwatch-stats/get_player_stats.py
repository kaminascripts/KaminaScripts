#!/usr/bin/env python

import overwatch.stats
import argparse
import socket
import time
import sys
import re

parser = argparse.ArgumentParser(description='Overwatch - get player statistics \nGraphite_schema: overwatch.user.game_mode.stats')
parser.add_argument('--userlist', help='File with users to get stats', dest="userlist", default='./userlist.txt')
args = parser.parse_args()

CARBON_SERVER = '0.0.0.0'
CARBON_PORT = 2003

def sent_stat(schema, user, stat, key, value):
    sock = socket.socket()
    sock.connect((CARBON_SERVER, CARBON_PORT))
    escaped_user = re.sub('[#]', '', user)
    message = 'overwatch.{}.{}{}{} {} {}\n'.format(escaped_user, stat, schema, key, value, int(time.time()))
    sock.sendall(message)
    sock.close()
    print message

with open(args.userlist) as f:
    users = f.read().splitlines()

for user in users:
    print "INFO - User selected:" + user + "\n"
    overwatch.stats.query('pc', 'eu', user)
    stats = overwatch.stats.query('pc', 'eu', user)
    for stat, value in stats.items():
        if stat == 'level' or stat == 'competitive_rank':
            schema = key = ''
            sent_stat(schema, user, stat, key, value)
            continue
        for key, value in stats[stat]['overall'].items():
            schema = '.overall.'
            sent_stat(schema, user, stat, key, value)

print "INFO - END\n"
