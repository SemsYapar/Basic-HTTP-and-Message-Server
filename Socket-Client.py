#Code by Sems

import socket

class TCPClient:
	#Hedef Client'in ip adresini ve giriceğimiz port numarasını yazıyoruz, boş bırakıp program içinde manuel olarakda belirliyebilirsiniz
	def __init__(self, host="192.168.1.34", port=8888):
		self.host = host
		self.port = port
		if self.host and self.port == None:
			self.host =input("Manuel olarak host adresini giriniz..  ")
			self.port =input("Manuel olarak port adresini giriniz..  ")

	def start(self):
		#Disconnect mesajı isteğe bağlı değiştirilebilir
		DISCONNECT="exit()"
		clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		clientsocket.connect((self.host, self.port))
		print(f"{self.host} {self.port} host adresine bağlanılmıştır.")
		server_msg = clientsocket.recv(1024).decode("utf-8")
		if server_msg:
		    print(f"Server: {server_msg}")

		while True:
			#Mesaj gönderme protokolümüz..
			msg =input("=>.. ")
			client_msg_size = str(len(msg.encode("utf-8")))
			clientsocket.send(bytes(client_msg_size,"utf-8"))
			clientsocket.send(bytes(msg,"utf-8"))
			#Disconnect protokolümüz..
			if msg == DISCONNECT:
				msg = f"{clientsocket.getsockname()} is exit the server.."
				clientsocket.send(bytes(msg,"utf-8"))
				print(msg)
				clientsocket.close()
				break
			#Mesaj alma protokolümüz
			server_resp_size = clientsocket.recv(8).decode("utf-8")
			server_resp_size = int(server_resp_size)
			response = clientsocket.recv(server_resp_size).decode("utf-8")
			if response:
				print("Server message: ", response)


if __name__ == "__main__":
	c = TCPClient()
	c.start()
