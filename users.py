#!/usr/bin/env python
from __future__ import print_function
from xmlrpclib import ServerProxy

SERVER = 'http://localhost:8069'
DATABASE = 'omega'
USERNAME = 'admin'
PASSWORD = 'omega'

server = ServerProxy('http://localhost:8069/xmlrpc/common')
user_id = server.login(DATABASE, USERNAME, PASSWORD)

server = ServerProxy('http://localhost:8069/xmlrpc/object')
user_ids = server.execute(
    DATABASE, user_id, PASSWORD,
    'res.users', 'search', []
)

users = server.execute(
    DATABASE, user_id, PASSWORD,
    'res.users', 'read', user_ids, []
)

for user in users:
    print(user['id'], user['name'], user['email'])
