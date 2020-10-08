#Sems Code
#Server

import socket

class TCPServer:
    def __init__(self, host):
        self.host = host
    def start(self):
        while True:
            self.port =input("HTTPServer için ""80"", EchoServer için ""8888"" port numarasını girin ")
            self.port = int(self.port)
            #HTTP Server' a geçiş..
            if self.port == 80:
                httpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                httpserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                httpserver.bind((self.host, self.port))
                httpserver.listen(5)
                print(f"Listening at {httpserver.getsockname()}  ")

                while True:
                    conn, addr = httpserver.accept()
                    print("Connected by", addr)
                    data = conn.recv(1024).decode("utf-8")
                    response = self.handle_request(data)
                    conn.sendall(bytes(response,"utf-8"))
                    conn.close()
            #Basit server-client mesajlaşma serverına geçiş..
            if self.port == 8888:
                DISCONNECT="exit()"
                tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tcpserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                tcpserver.bind((self.host, self.port))
                tcpserver.listen(5)
                print("Listening at", tcpserver.getsockname())
                while True:
                    conn, addr = tcpserver.accept()
                    print("Connected by", addr)
                    conn.send(bytes("""Sems Server'a Hoşgeldin! Bana istediğini yazabilirsin\n
                    NOT: Serverdan çıkmak için ""exit()"" yazınız..""","utf-8"))
                    while True:
                        client_msg_size = conn.recv(8).decode("utf-8")
                        client_msg_size = int(client_msg_size)
                        msg = conn.recv(client_msg_size).decode("utf-8")
                        print("Client message: ", msg)
                        if msg == DISCONNECT:
                            msg = conn.recv(64).decode("utf-8")
                            print(msg)
                            conn.close()
                            break
                        response =input("=>.. ")
                        server_resp_size = str(len(response.encode("utf-8")))
                        conn.send(bytes(server_resp_size,"utf-8"))
                        conn.send(bytes(response,"utf-8"))
            
            else:
                print("Geçersiz bir port verdiniz, nütfen tekrar deneyin..")


    def handle_request(self, data):
        """Handles incoming data and returns a response.
        Override this in subclass.
        """
        return data

class HTTPServer(TCPServer):


    def handle_request(self,data):
        #HTTP başlığı ve mesajı hazırlama fonksiyonu..
        headers={
            "Server": "Sems Server",
            "Content-Type": "text/html",
        }

        status_code={
            "200": "OK",
            "404": "Not Found",
        }

        response_line = self.response_line(status_code="200")
        response_headers = self.response_headers()

        blank_line = "\r\n"

        response_body = """
            <html>
                <body>
                    <h1>Hi Man Whats Up</h1>
                </body>
            </html>
        """

        return  response_line+blank_line+response_headers+response_body

    def response_line(self, status_code):

        reason = self.status_code[status_code]
        return f"HTTP/1.1 {status_code} {reason}"

    def response_headers(self, extra_headers=None):

        headers_copy = self.headers.copy()

        if extra_headers:
            headers_copy.update(extra_headers)

        headers = ""

        for h in self.headers:

            headers += f"{h}: {self.headers[h]}\n"
        return headers

if __name__ == '__main__':
    #Bilgisiyarınız local ip adresini giriniz..
    server = HTTPServer("192.168.1.34")
    server.start()
