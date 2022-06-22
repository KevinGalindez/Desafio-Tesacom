import struct

def decodificar_dato(dato, tipo):

    if tipo == "int":

        return int.from_bytes(dato, byteorder="big", signed=False)

    elif tipo == "float":

        floatt = struct.unpack("f", bytes(dato))
        float_real = floatt[0]
        return float_real

    elif tipo == "str":

        strin = bytes(dato)
        strings = strin.decode("utf-8")
        return strings
    else:
        return None

def decodificar_trama(trama, formato):
    resultado = {}
    bytes_arr = list(bytes(trama))
    for sub_formato in formato:
        size = int(sub_formato["len"] / 8)
        dato = bytes_arr[:size]
        del bytes_arr[:size]

        val = decodificar_dato(dato, sub_formato["type"])

        if val is None:
            return None

        resultado[sub_formato["tag"]] = val
    return resultado

def codificar_dato(dato, tamaño, tipo):

    if tipo == "int":
        if type(dato) is int or float:
            x = int(dato)
            result = x.to_bytes(int(tamaño / 8), "big")
            return result
        elif type(dato) is str:
            return None

    elif tipo == "float":
        if type(dato) is int or float:
            x = float(dato)
            result = struct.pack("f", dato)
            return result
        else:
            return None

    elif tipo == "str":
        if type(dato) is int or float:
            x = str(dato)
            result = bytes(dato, "utf-8")
            return result
        elif type(dato) is str:
            result = bytes(dato, "utf-8")
            return result
    else:
        return None

def codificar_trama(dicc, formato):

    buffer = b""

    for valor, sub_formato in zip(dicc.values(), formato):
        result = codificar_dato(valor, sub_formato["len"], sub_formato["type"])
        if result is None:
            return None
        else:
            buffer = buffer + result
    return buffer

formato1 = [
    {"tag": "v0", "type": "str", "len": 8},
    {"tag": "v1", "type": "float", "len": 32},
    {"tag": "v2", "type": "int", "len": 8},
]
formato2 = [
    {"tag": "v0", "type": "int", "len": 8},
    {"tag": "v1", "type": "int", "len": 16},
]
formato3 = [
    {"tag": "v0", "type": "int", "len": 8},
    {"tag": "v1", "type": "int", "len": 40},
    {"tag": "v2", "type": "float", "len": 32},
    {"tag": "v3", "type": "str", "len": 64},
]

trama_ejemplo = b"\x40\x32\x03\x04\x05\x06"

diccionario_valores_ejemplo = {
    "voltaje": 65,
    "frecuencia": 300,
    "temp": 28.42,
    "Version": "C0123ABC",
}

print(diccionario_valores_ejemplo)
print()

prueba1 = codificar_trama(diccionario_valores_ejemplo, formato3)

if prueba1 is None:
    print("Ha ocurrido un error")
else:
    print(prueba1)
    print()

prueba01 = decodificar_trama(prueba1, formato3)

if prueba01 is None:
    print("Ha ocurrido un error")
else:
    print(prueba01)


