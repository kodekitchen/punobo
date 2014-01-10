#!/usr/bin/pyhton

import xmpp
import sys

jid = xmpp.protocol.JID('...@jabber.ccc.de')
psswrd = '...'

recipients = ['...@jabber.ccc.de']
msg = 'Push-Notification\n------------\n' + sys.argv[1]

client = xmpp.Client(jid.getDomain(), debug=[])
client.connect()
client.auth(jid.getNode(), psswrd)
for recipient in recipients:
    client.send(xmpp.protocol.Message(recipient, msg))
