from Encodes import Encode
from Encodes.Reverse import Reverse


class Message:

    def __init__(self, message: str, encoding: Encode = None, encryptd: Boolean = False):
        self._message = message
        self._encrypted = encryptd
        self._objectEncode = encoding

    def encode(self):
        if self._objectEncode is None:
            raise ValueError("Encoding is not set")
        elif self._encrypted:
            raise ValueError("Message is encrypted")

        message = self._objectEncode.encode(self._message)
        return Message(message, self._objectEncode, True)

    def decode(self):
        if self._objectEncode is None:
            raise ValueError("Encoding is not set")
        if not self._encrypted:
            raise ValueError("Message is not encrypted")

        message = self._objectEncode.decode(self._message)
        return Message(message, self._objectEncode, False)
        
    def set_encoding(self, encoding: Encode):
        if self._objectEncode:
            raise ValueError("Encoding is already set")

        self._objectEncode = encoding
        return self

    def get_encoding(self):
        return self._objectEncode

    def is_encrypted(self):
        return self._encrypted

    def __str__(self):
        return self._message

    def __repr__(self):
        return f"Message(text={self._message}, encode={self._objectEncode.__class__.__name__}, encrypted={self._encrypted})"
