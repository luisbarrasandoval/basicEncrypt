from Message import Message
from Encodes import list_encodes


def show_encodes():
    for i, encode in enumerate(list_encodes, 1):
        if encode.required_password():
            print(
                f"{i} - {encode.__name__} (requiere password: {encode.password_type().__name__})")
        else:
            print(f"{i} - {encode.__name__}")


def main():
    print("Selecione el tipo de codificacion (q para salir)")

    while True:
        show_encodes()
        entrada = input(">> ")
        if entrada == "q":
            break

        try:
            opcion = int(entrada) - 1
        except ValueError:
            print("Opcion invalida")
            continue

        if opcion < 0 or opcion >= len(list_encodes):
            print("Opcion invalida")
            continue

        encode = list_encodes[opcion]
        if encode.required_password():
            password = input(
                f"Password ({ encode.password_type().__name__ }): ")
            password = encode.password_type()(password.strip())
            encode = encode(password)
        else:
            encode = encode()

        data = input("Message: ")
        message = Message(data)
        message.set_encoding(encode)
        result = message.encode()
        print("=" * 80)
        print(result)
        print("=" * 80)


if __name__ == "__main__":
    main()
