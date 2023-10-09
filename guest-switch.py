# THIS IS THE GUEST MACHINE CODE

import socket
import nxbt

HOST = "10.0.2.2"  # VirtualBox's default gateway IP for the host machine when using NAT networking
PORT = 65432  # Same port as used by the server

nx = nxbt.Nxbt()

controller_index = nx.create_controller(nxbt.PRO_CONTROLLER)
nx.wait_for_connection(controller_index)

print("Connected To Switch")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        # Send data to the host machine here
        s.sendall(b"Hello from VM!")
