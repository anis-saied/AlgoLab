import subprocess
import time

# Commands to establish SSH tunnel
ssh_tunnel_command = "ssh -L 3307:foartci638.mysql.db:3306 amsgpqv@ssh.cluster030.hosting.ovh.net"

# Execute SSH tunnel command in a subprocess
ssh_tunnel_process = subprocess.Popen(ssh_tunnel_command, shell=True)

# Sleep for a few seconds to allow SSH tunnel to establish
time.sleep(5)

# MySQL command including password
mysql_command = "mysql -u foartci638 -pyour_password -h 127.0.0.1 -P 3307 -e \"use foartci638; SHOW TABLES;\""

# Execute MySQL command in a subprocess
mysql_process = subprocess.Popen(mysql_command, shell=True)

# Wait for MySQL process to finish
mysql_process.wait()

# Terminate the SSH tunnel process
ssh_tunnel_process.terminate()
