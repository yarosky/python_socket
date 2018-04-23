import socket, struct, time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = input("Enter HOST (e.g. 127.0.0.1): ")
PORT = 2306
RECV_BUFFER = 4096

s.connect((HOST, PORT))
print("Connect to the host: %s:%s" % (HOST, PORT))
attempts = 4
seq_num = 0
while seq_num != attempts:
    seq_num += 1
    pdata = struct.pack("!Hd", seq_num, time.time())
    s.send(pdata)
    data = s.recv(RECV_BUFFER)
    current_time = time.time()
    (seq, timestamp) = struct.unpack("!Hd", data)
    time_dff = current_time - timestamp
    time_dff *= 1000

    print ("seq=%u, time_dff=%.3f ms" % (seq, time_dff))
    time.sleep(1)
s.close()