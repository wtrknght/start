import os
os.path.expanduser('~')
g = os.environ.get('USERNAME')
r = (f'/home/{g}/os.environ.get(\'USERNAME\')')
f = open(r, 'w')
f.write('#Gmail account

defaults
#change the location of the log file to any desired location.
logfile ~/msmtp.log
account gmail
auth on
host smtp.gmail.com
auth on
tls on
tls_trust_file /usr/share/ca-certificates/mozilla/Equifax_Secure_CA.crt
user wyattkinard1@gmail.com
password EEEEaaaa1@
port 587
#set gmail as your default mail server.
account default : gmail')
f.close()
quit()
