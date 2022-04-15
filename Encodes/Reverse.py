from .Encode import Encode


class Reverse(Encode):

    def encode(self, data):
        return data[::-1]

    def decode(self, data):
        return data[::-1]
