import socket

def receive_tcp_packet(server_address, server_port):
    # Создаем TCP-сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Устанавливаем соединение с сервером
        client_socket.connect((server_address, server_port))

        # Получаем TCP-пакет
        packet = b''  # Переменная для хранения собранного пакета
        expected_packet_length = 0  # Ожидаемая длина пакета

        while True:
            received_data = client_socket.recv(4096)  # Читаем данные из сокета

            if not received_data:
                break  # Если данные не получены, выходим из цикла

            packet += received_data  # Добавляем принятые данные к собранному пакету

            if expected_packet_length == 0:
                # Если ожидаемая длина пакета еще не установлена, извлекаем ее из заголовка
                if len(packet) >= 16:  # Минимальная длина заголовка TCP-пакета
                    data_offset = (packet[12] >> 4) * 4
                    expected_packet_length = data_offset + 1  # Длина заголовка + 1 байт для оконечного флага

            if len(packet) >= expected_packet_length:
                break  # Если длина собранного пакета достигла ожидаемой, прекращаем чтение

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
