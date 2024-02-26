import socket

def send_empty_tcp_packet(client_socket):
    # Отправляем пустой TCP-пакет в ответ
    client_socket.send(b'')

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
        
        # Отправляем пустой TCP-пакет
        send_empty_tcp_packet(client_socket)
        
        # Закрываем соединение с клиентом
        client_socket.close()

if __name__ == '__main__':
    start_server()
