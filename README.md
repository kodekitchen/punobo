Make Script executable and call python <somepath>/pushbot.py "Message about push" from post-receive hook on remote git repository.

Second argument is key that shall be popped when sending messages. Intended for excluding commiter from message queue.

Example

In pushbot.py add recipients to list, like

     rcps_list={'ConcernedCommmiter' : 'recipient@jabber'}

In hooks/post-receive do something like:

     > exclude=`git log -1 --pretty=format:"%cn"`
     > python <...>/pushbot.py "Commit to <x> pushed!" ${exclude}

If ConcernedCommiter is pushing to the repository he is ommited from the message queue.



requires python-xmpppy 

...and python :-)
