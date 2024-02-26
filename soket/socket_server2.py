import socket

def send_tcp_packet(client_socket, data):
    # Отправляем данные в виде TCP-пакета в ответ
    client_socket.send(data)

def start_server():
    # Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Привязываем сокет к адресу и порту
    server_address = ('', 8001)
    server_socket.bind(server_address)
    
    # Слушаем входящие подключения
    server_socket.listen(1)
    
    print('Сервер запущен и слушает порт 8001...')
    
    while True:
        # Принимаем входящее подключение
        client_socket, client_address = server_socket.accept()
        print('Получено входящее подключение от:', client_address)
        
        # Отправляем номер "1003105FD020" в виде TCP-пакета
        number = "1003105FD020"
        ascii_encoded = number.encode('ascii')
        send_tcp_packet(client_socket, ascii_encoded)
        
        # Закрываем соединение с клиентом
        client_socket.close()

if __name__ == '__main__':
    start_server()
