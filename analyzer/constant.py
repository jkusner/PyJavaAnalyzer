from .util import *

import struct

class Constant:
    STRING = 1
    INT = 3
    FLOAT = 4
    LONG = 5
    DOUBLE = 6
    CLASSREF = 7
    STRINGREF = 8
    FIELDREF = 9
    METHODREF = 10
    INTERFACEMETHODREF = 11
    NAMEANDTYPE = 12
    METHODHANDLE = 15
    METHODTYPE = 16
    INVOKEDYNAMIC = 18

    def __init__(self, data, index):
        self.data = data
        self.index = index

        # self.index, data = ClassFile._read_short(data)
        # print(self.index)

        # self.data = data = data[1:]

        self.type = data[0]

        self.data = data = data[1:]

        self._msg = self.msg = None

        # Check the type of the data
        if self.type == Constant.STRING:
            self._read_string()
        elif self.type == Constant.INT:
            self._read_int()
        elif self.type == Constant.FLOAT:
            self._read_float()
        elif self.type == Constant.LONG:
            self._read_long()
        elif self.type == Constant.DOUBLE:
            self._read_double()
        elif self.type == Constant.CLASSREF:
            self._read_classref()
        elif self.type == Constant.STRINGREF:
            self._read_stringref()
        elif self.type == Constant.FIELDREF:
            self._read_fieldref()
        elif self.type == Constant.METHODREF:
            self._read_methodref()
        elif self.type == Constant.INTERFACEMETHODREF:
            self._read_interfacemethodref()
        elif self.type == Constant.NAMEANDTYPE:
            self._read_nameandtype()
        elif self.type == Constant.METHODHANDLE:
            self._read_methodhandle()
        elif self.type == Constant.METHODTYPE:
            self._read_methodtype()
        elif self.type == Constant.INVOKEDYNAMIC:
            self._read_invokedynamic()
        else:
            print("Couldn't parse constant. Type=", self.type)

        self._msg = self.msg

        # if self.msg is not None:
        # print(self.msg)
        # else:
        # print("error: type: ", self.type)

    def _read_string(self):
        bites, data = read_u2(self.data)
        # java utf-8 is weird i will deal with that later (TODO)

        # print("string length = ", bites)

        msg = data[:bites].decode("utf-8")

        self.data = data[bites:]
        self.msg = msg

    def _read_int(self):
        self.msg = struct.unpack(">i", self.data[:4])[0]
        self.data = self.data[4:]

    def _read_float(self):
        self.msg = struct.unpack(">f", self.data[:4])[0]
        self.data = self.data[4:]

    def _read_long(self):
        self.msg = struct.unpack(">q", self.data[:8])[0]
        self.data = self.data[8:]

    def _read_double(self):
        self.msg = struct.unpack(">d", self.data[:8])[0]
        self.data = self.data[8:]

    def _read_classref(self):
        self.msg, self.data = read_u2(self.data)

    def _read_stringref(self):
        self.msg, self.data = read_u2(self.data)

    def _read_fieldref(self):
        self.msg, self.data = read_u2(self.data)
        temp, self.data = read_u2(self.data)
        self.msg += temp

    def _read_methodref(self):
        self.msg, self.data = read_u2(self.data)
        temp, self.data = read_u2(self.data)
        self.msg += temp

    def _read_interfacemethodref(self):
        self.msg, self.data = read_u2(self.data)
        temp, self.data = read_u2(self.data)
        self.msg += temp

    def _read_nameandtype(self):
        self.msg, self.data = read_u2(self.data)
        temp, self.data = read_u2(self.data)
        self.msg += temp

    def _read_methodhandle(self):
        # TODO
        self.msg = "methodhandle, unread."
        self.data = self.data[3:]

    def _read_methodtype(self):
        self.msg, self.data = read_u2(self.data)
        temp, self.data = read_u2(self.data)
        self.msg += temp

    def _read_invokedynamic(self):
        self.msg = "Invoke Dynamic, unread."
        self.data = self.data[4:]

    def _solve_ref(self, pool):
        if self.type == Constant.CLASSREF:
            # msg is pointing to string index.
            self.msg = pool[self.msg].msg
        elif self.type == Constant.METHODREF:
            # TODO
            self.msg = "MethodRef - TODO"
        elif self.type == Constant.INTERFACEMETHODREF:
            # TODO
            self.msg = "InterfaceMethodRef - TODO"
        elif self.type == Constant.FIELDREF:
            # TODO
            self.msg = "FieldRef - TODO"
        elif self.type == Constant.STRINGREF:
            # msg is pointing to string index
            self.msg = pool[self.msg].msg

