from twisted.internet import protocol, reactor

class MyProtocol(protocol.Protocol):
    def dataReceived(seld, data):
        # Обработка плдученных данных
        self.transport.write(data)  # Отправка ответа

class MyFacrory(protocol.Factory):
    def buildProtocol(self, addr):
        return MyProtocol()

if __name__ == "__main__":
    reactor.listenTCP(12345, MyFactory())
    reactor.run()
