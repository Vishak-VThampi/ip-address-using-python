import socket
hostn= socket.gethostname()
ipadd= socket.gethostbyname(hostn)
print("IP Address is "+ipadd)
