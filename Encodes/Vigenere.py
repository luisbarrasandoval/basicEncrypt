from .Encode import Encode


class Vigenere(Encode):

    def __init__(self, password: str):
        super().__init__(password)

    def encode(self, data):
        return "".join([chr((ord(char) + ord(self.password[i % len(self.password)])) % 256) for i, char in enumerate(data)])

    def decode(self, data):
        return "".join([chr((ord(char) - ord(self.password[i % len(self.password)])) % 256) for i, char in enumerate(data)])


if __name__ == "__main__":
    m = Vigenere("hola")
    message = "Hola Mundo"
    print(m.encode(message))
    print(m.decode(m.encode(message)))
