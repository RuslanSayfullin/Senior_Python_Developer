import socket

def receive_tcp_packet(server_address, server_port):
    # Создаем TCP-сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Устанавливаем соединение с сервером
        client_socket.connect((server_address, server_port))

        # Получаем TCP-пакет
        packet = client_socket.recv(4096)  # Указываем максимальный размер пакета, в данном случае 4096 байт

        # Сохраняем пакет в файл
        with open('received_packet.bin', 'wb') as file:
            file.write(packet)

        print("Получен TCP-пакет и сохранен в файл 'received_packet.bin'")
    
    finally:
        # Закрываем соединение
        client_socket.close()

if __name__ == '__main__':
    server_address = '192.168.1.45'
    server_port = 8001

    receive_tcp_packet(server_address, server_port)

