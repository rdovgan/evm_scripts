def convert_to_id(x: int, y: int):
    return (y << 8) + x


def convert_to_coordinates(id_dec: int):
    return id_dec & 255, id_dec >> 8

