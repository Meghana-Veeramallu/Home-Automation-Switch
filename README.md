# Home Automation Switch Using Raw Sockets
A Multi-threaded client-server system where multiple clients can access a single server[appliances] and control the status of the  appliances.

Has: 

-> Simple user UI with additional features like – set timer, schedule an appliance, add/remove an appliance to the system. 

-> TCP connection with SSL certificate verification by both server 
and client.

# Steps to follow:
Follow these steps to run your client-server home automation switch

## Run cert.py  
```
python cert.py
```
Run this code to generate the .crt and .key files required to set up a secured protected connection for your client and the server.

Make sure that both the server and client have the ca.crt and ca.key files where as the server and client have their respective .crt and .key files.

## Run server.py
```
python server.py
```
Before you run, this code has pre-defined 'user: password' values to be mentioned. Edit your code to your desired client users and their respective passwords and then run the file.

## Run client.py
```
python client.py
```
This code can be run by multiple clients.

Make sure you enter the proper server IP address in the mentioned slot.

You can know your server IP address by runnin gthe following command in the command prompt.
```
ipconfig
```
Use the Ipv4 address from the output.
