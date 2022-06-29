# import struct
from bitstring import BitArray

def decodificar_dato(dato, tipo):

    if tipo == "int":

        entero = dato.int
        return entero

    elif tipo == "float":

        float_real = dato.float
        return float_real

    elif tipo == "str":

        dato_string = dato.hex
        datos_bytes = bytes.fromhex(dato_string)
        ascii_strings = datos_bytes.decode("utf-8")
        return ascii_strings
    else:
        return None

def decodificar_trama(trama, formato):
    resultado = {}
    bytes_arr = BitArray(trama)
    for sub_formato in formato:
        size = int(sub_formato["len"])
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
            result = BitArray(int=dato, length=tamaño)
            return result
        elif type(dato) is str:
            return None

    elif tipo == "float":
        if type(dato) is int or float:
            x = float(dato)
            result = BitArray(float=x, length=tamaño)
            return result
        else:
            return None

    elif tipo == "str":
        if type(dato) is int or float:
            x = str(dato)
            result = bytes(x, "utf-8")
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
    {"tag": "v0", "type": "str", "len": 32},
    {"tag": "v1", "type": "float", "len": 32},
    {"tag": "v2", "type": "int", "len": 8},
]
formato2 = [
    {"tag": "v0", "type": "int", "len": 4},
    {"tag": "v1", "type": "int", "len": 6},
]
formato3 = [
    {"tag": "v0", "type": "int", "len": 9},
    {"tag": "v1", "type": "int", "len": 19},
    {"tag": "v2", "type": "float", "len": 64},
    {"tag": "v3", "type": "str", "len": 16},
]

# trama_ejemplo = b"\x40\x32\x03\x04\x05\x06"

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


