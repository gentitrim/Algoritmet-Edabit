import socket
def get_domain(ip_address):
	name ,a , address = socket.gethostbyaddr(ip_address)
	return name , a , address
print(get_domain("8.8.8.8"))