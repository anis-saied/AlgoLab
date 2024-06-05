#!/bin/bash

python3 extract-all-new-products.py
python3 filter-only-i7-13e-gen.py
python3 extract-prices.py
node filter_and_sort.js

# Open index.html in Firefox

# Start the Python HTTP server in the background
python3 -m http.server &

# Store the server's process ID (PID)
server_pid=$!

# Sleep briefly to allow the server to start
sleep 2

# Open the URL in Firefox (change the URL as needed)
firefox http://0.0.0.0:8000/index.html

# Wait for user to finish in the browser
read -p "Press Enter to stop the server and exit..."

# Terminate the Python HTTP server
kill $server_pid


