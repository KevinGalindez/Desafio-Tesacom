import struct

def decodificar_dato(dato, type):

    if type == "int":

        return int.from_bytes(dato, byteorder="big", signed=False)

    elif type == "float":

        floatt = struct.unpack("f", bytes(dato))
        float_real = floatt[0]
        return float_real

    elif type == "str":

        strin = bytes(dato)
        strings = strin.decode("utf-8")
        return strings

def decodificar_trama(trama, formato):
    resultado = {}
    bytes_arr = list(bytes(trama))
    for sub_formato in formato:
        size = int(sub_formato["len"] / 8)
        dato = bytes_arr[:size]
        del bytes_arr[:size]

        val = decodificar_dato(dato, sub_formato["type"])
        resultado[sub_formato["tag"]] = val
    return resultado


trama = b"\x40\x32\x03\x04\x05\x06"
formato1 = [
    {"tag": "v0", "type": "str", "len": 8},
    {"tag": "v1", "type": "float", "len": 32},
    {"tag": "v2", "type": "int", "len": 8},
]
formato2 = [
    {"tag": "v0", "type": "int", "len": 8},
    {"tag": "v1", "type": "int", "len": 16},
]

print(decodificar_trama(trama, formato1))
print(decodificar_trama(trama, formato2))
