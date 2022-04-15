from abc import ABC, abstractmethod


class Encode(ABC):
    password = None

    def __init__(self, password=None):
        self.password = password

    @abstractmethod
    def encode(self, data) -> str:
        raise NotImplementedError

    @abstractmethod
    def decode(self, data) -> str:
        raise NotImplementedError

    @classmethod
    def required_password(cls):
        return cls.__init__.__annotations__.get('password') is not None

    @classmethod
    def password_type(cls):
        return cls.__init__.__annotations__.get('password')
