# Install
pip install -r requirements.txt

# Overview
This project implements a simple REST API using Flask, allowing users to monitor the availability of IP addresses by pinging them. Users can add or remove IP addresses to be monitored, and the API provides endpoints to fetch the list of IPs, add new IPs, and remove existing ones.

# Features

Check IP Availability: The API includes functionality to ping IP addresses and determine whether they are reachable or not.
Add IPs: Users can add new IP addresses to the monitoring list.
Remove IPs: Existing IP addresses can be removed from the monitoring list.
Dependencies:

Flask: A lightweight web framework for Python used to create the REST API endpoints.
subprocess: A module used to run system commands, in this case, to execute the ping command.
json: A module for encoding and decoding JSON data.
How to Run:

# Install 
pip install -r requirements.txt.

# Run
Run the Flask application by executing the script. The API will be accessible at http://localhost:5000 by default.

# Usage
Use HTTP requests to interact with the API, such as GET, POST, and DELETE, to manage the list of monitored IP addresses.


# Endpoints:

GET /ips: Retrieve the list of monitored IP addresses.
POST /ips: Add a new IP address to the monitoring list.
DELETE /ips/<ip>: Remove an existing IP address from the monitoring list.
Usage:

Users can send HTTP requests to the respective endpoints to manage the monitored IP addresses.
Example usage:
To add a new IP: POST /ips with JSON data {"ip": "xxx.xxx.xxx.xxx"}.
To remove an IP: DELETE /ips/xxx.xxx.xxx.xxx.
To fetch all IPs: GET /ips.

# Notes

This project assumes that IPs are stored in a JSON file named ips.json in the same directory as the script.
Ensure proper error handling and security measures are implemented before deploying the API in a production environment.