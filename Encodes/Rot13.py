from .Encode import Encode
from .Cesar import Cesar


class Rot13(Cesar):

    def __init__(self):
        super().__init__(13)


if __name__ == "__main__":
    m = Rot13()
    message = "Hola Mundo"
    print(m.encode(message))
    print(m.decode(m.encode(message)))
