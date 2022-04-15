from .Encode import Encode
import dics


class Morse(Encode):

    def encode(self, data):
        return " ".join([dics.MORSE[char] for char in data.upper() if char != ' '])

    def decode(self, data):
        return "".join([dics.MORSE_REVERSE[char] for char in data.split()])


if __name__ == "__main__":
    m = Morse()
    message = "Hola Mundo"
    print(m.encode(message))
    print(m.decode(m.encode(message)))
