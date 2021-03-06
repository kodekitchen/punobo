#!/usr/bin/pyhton

import xmpp
import sys

jid = xmpp.protocol.JID('...@jabber.ccc.de')
psswrd = '...'

rcps_list = ['some_key' : 'jabber_name@server' ]
try:
	del rcps_list[sys.argv[2]]
except KeyError:
	pass

recipients = []

for key, value in rcps_list.iteritems():
	recipients.append(value)

msg = 'Push-Notification\n------------\n' + sys.argv[1]

client = xmpp.Client(jid.getDomain(), debug=[])
client.connect()
client.auth(jid.getNode(), psswrd)
for recipient in recipients:
    client.send(xmpp.protocol.Message(recipient, msg))
