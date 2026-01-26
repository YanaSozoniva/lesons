def up_first(msg):
    """Делает первую букву строки заглавной."""
    if msg:
        return msg[0].upper() + msg[1:]
    else:
        return msg


def reverse_string(my_str: str) -> str:
    return my_str[::-1]
