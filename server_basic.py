from socket import *

def createServer():

    # make the phone, not the phone call
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        # only 1 app gets the phone call on this port 9000
        serversocket.bind(('localhost', 9000))
        # can only hold 5 quess, one at a time
        serversocket.listen(5)
        while(1):
            
            # made the connection here
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if (len(pieces) > 0):
                print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            # need to be encoded ( utf-8)
            clientsocket.sendall(data.encode())
            
            # after sending he data it must be closed
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    serversocket.close()


print('Access http://localhost:9000')
createServer()
