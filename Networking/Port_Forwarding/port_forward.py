#Port forwarder simply:
#1) listens on a local_port (for TCP/UDP traffic)
#2) whatever traffic hits that port - forward to another designated remote_host:remote_port
#3) make sure that your client app is sending data to local_ip:local_port - but make sure the app intends for the data to hit remote_host:remote_port 
import socket
import threading

def forwarder(source, destination):
    try:
        while True:
            data = source.recv(4096)
            if not data:
                break
            destination.sendall(data)
    except Exception as e:
        print(f"Error forwarding data: {e}")
    finally:
        source.close()
        destination.close()


def port_forwarder(listen_host, listen_port, dest_host, dest_port):
    try:
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.bind((listen_host, listen_port))
        listen_socket.listen(5)
        print(f"Listening on {listen_host}:{listen_port} for connections to {dest_host}:{dest_port}")

        while True:
            client_socket, client_address = listen_socket.accept()
            print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

            dest_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            dest_socket.connect((dest_host, dest_port))

            #One thread to forward to client
            thread1 = threading.Thread(target=forwarder, args=(client_socket, dest_socket))
            #One thread to forward to dest
            thread2 = threading.Thread(target=forwarder, args=(dest_socket, client_socket))

            thread1.start()
            thread2.start()

    except KeyboardInterrupt:
        print("Port forwarder stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        listen_socket.close()


if __name__ == "__main__":
    #This will listen on all local network interfaces, port 8080 and forward traffic DESTINATION_PORT
    #TODO replace destination port
    port_forwarder("0.0.0.0", 8080, "<DESTINATION_IP>", 80)
