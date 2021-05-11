# Deploy mysql-server in automated way on Ubuntu VM
import os

require = open('requirements.txt')
requireContents = require.readlines()
require.close()

for i in range(0,len(requireContents)):
    os.system("pip3 install" + requireContents[i])

import socket
import subprocess

os.system("sudo apt-get update")
os.system("sudo apt-get install mysql-server")

# Firewal Rules

os.system("sudo ufw enable")
os.system("sudo ufw allow mysql")

# Modify mysql config file

mySQLConfig = open("/etc/mysql/my.cnf")
contentsList = mySQLConfig.readlines()
mySQLConfig.close()

contentsList.append("bind-address=" + socket.gethostbyname(socket.getfqdn()))

mySQLConfig = open("/etc/mysql/my.cnf", "w")
mySQLConfigContents = "".join(contentsList)

mySQLConfig.write(mySQLConfigContents)
mySQLConfig.close()

# Start Service

os.system("systemctl start mysql")

# Execute the script sqlZoomDB.sql on server

os.system("source sqlZoomDB.sql") 

# statement = ""

# for line in open("sqlZoomDB.sql"):
#     if line.strip().startswith('--'):  # ignore sql comment lines
#         continue
#     if not line.strip().endswith(';$'):  # keep appending lines that don't end in ';'
#         statement = statement + line
#     else:  # when you get a line ending in ';' then exec statement and reset for next statement
#         statement = statement + line
#             #print "\n\n[DEBUG] Executing SQL statement:\n%s" % (statement)
#         try:
#             cursor.execute(statement)
#         except (OperationalError, ProgrammingError) as e:
#             print("\n[WARN] MySQLError during execute statement \n\tArgs: '%s'" % (str(e.args)))

#         statement = ""