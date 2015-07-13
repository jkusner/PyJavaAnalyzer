import struct

def read_u2(data):
    """
    Reads a u2 from the data. (Unsigned short)
    :param data: Binary class file data
    :return: Unsigned short, trimmed data
    """
    return struct.unpack(">H", data[:2])[0], data[2:]

def read_u4(data):
    """
    Reads a u4 from the data. (Unsigned int)
    :param data: Binary class file data
    :return: Unsigned int, data
    """
    return struct.unpack(">I", data[:4])[0], data[4:]
