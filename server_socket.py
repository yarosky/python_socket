import socket, select

if __name__ == "__main__":

    CONNECTION_LIST = []
    RECV_BUFFER = 4096
    PORT = 2306

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", PORT))
    s.listen()
    CONNECTION_LIST.append(s)
    print("Server is started on port " + str(PORT))

    while True:
        read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])
        for sock in read_sockets:
            if sock == s:
                c, addr = s.accept()
                CONNECTION_LIST.append(c)
                print("Client (%s, %s) connected" % addr)
            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        sock.send(data)
                    else:
                        raise ConnectionResetError()
                except:
                    print("Client (%s, %s) is disconnected" % addr)
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue


