from .Encode import Encode


class Cesar(Encode):

    def __init__(self, password: int):
        super().__init__(password)

    def encode(self, data):
        return "".join([chr((ord(char) + self.password) % 256) for char in data])

    def decode(self, data):
        return "".join([chr((ord(char) - self.password) % 256) for char in data])


if __name__ == "__main__":
    m = Cesar(5)
    message = "Hola Mundo"
    print(m.encode(message))
    print(m.decode(m.encode(message)))
