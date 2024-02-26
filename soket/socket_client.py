import socket

def analyze_tcp_packet(packet):
    if len(packet) >= 20:  # Минимальная длина TCP-пакета
        # Анализируем структуру TCP-пакета
        source_port = int.from_bytes(packet[0:2], byteorder='big')
        destination_port = int.from_bytes(packet[2:4], byteorder='big')
        sequence_number = int.from_bytes(packet[4:8], byteorder='big')
        acknowledgment_number = int.from_bytes(packet[8:12], byteorder='big')
        data_offset = (packet[12] >> 4) * 4
        flags = packet[13]
        window_size = int.from_bytes(packet[14:16], byteorder='big')
        checksum = int.from_bytes(packet[16:18], byteorder='big')
        urgent_pointer = int.from_bytes(packet[18:20], byteorder='big')

        # Выводим информацию о структуре пакета
        print('Информация о TCP-пакете:')
        print('Source Port:', source_port)
        print('Destination Port:', destination_port)
        print('Sequence Number:', sequence_number)
        print('Acknowledgment Number:', acknowledgment_number)
        print('Data Offset:', data_offset)
        print('Flags:', flags)
        print('Window Size:', window_size)
        print('Checksum:', checksum)
        print('Urgent Pointer:', urgent_pointer)
    else:
        print('Ошибка: недостаточно данных для анализа TCP-пакета')

def request_tcp_packet():
    # Создаем TCP-сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Устанавливаем соединение с сервером
    server_address = ('192.168.1.45', 8001)
    client_socket.connect(server_address)
    
    # Отправляем запрос на получение TCP-пакета
    client_socket.send(b'Request')
    
    # Получаем TCP-пакет
    packet = client_socket.recv(1024)
    print(packet, len(packet))

    # Сохраняем данные пакета в файл
    with open('my_data.txt', 'wb') as file:
        file.write(packet)
    
    # Анализируем структуру TCP-пакета
    #analyze_tcp_packet(packet)
    
    # Закрываем соединение с сервером
    client_socket.close()

if __name__ == '__main__':
    request_tcp_packet()
