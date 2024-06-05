#!/bin/bash

python3 extract-only-i7-13e-gen.py
python3 extract-products-infos.py
python3 filter_sort.py


# Open index.html in Firefox

# Start the Python HTTP server in the background
python3 -m http.server 8080 &

# Store the server's process ID (PID)
server_pid=$!

# Sleep briefly to allow the server to start
sleep 2

# Open the URL in Firefox (change the URL as needed)
firefox http://0.0.0.0:8080/index.html

# Wait for user to finish in the browser
read -p "Press Enter to stop the server and exit..."

# Terminate the Python HTTP server
kill $server_pid


