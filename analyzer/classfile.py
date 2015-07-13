from .constantpool import ConstantPool
from .method import Method
from .field import Field
from .attribute import Attribute
from .accessflags import AccessFlags
from .util import *

import struct

class ClassFile:
    def __init__(self, data):
        """
        Creates a ClassFile from class file data.
        :param data: Raw binary class file data
        """

        self.data = data

        # Read 4 byte magic. Should be 0xCAFEBABE
        self.magic, data = read_u4(data)

        if self.magic != 0xCAFEBABE:
            print("Invalid class file... still trying to parse")

        # Read 2 byte minor version and major version.
        self.minor_version, data = read_u2(data)
        self.major_version, data = read_u2(data)

        print("Major version: %s, Minor version: %s" % (self.major_version, self.minor_version))

        # Read constant pool count
        self.cpcount, data = read_u2(data)
        cpcount = self.cpcount
        print("cpcount =", cpcount)

        # Get the constant pool
        self.constant_pool = ConstantPool(cpcount, data)
        self.constants = self.constant_pool.get_constants()

        data = self.constant_pool.get_data()

        self.access_flags, data = self._read_access_flags(data)
        print("flags:", self.access_flags)

        this_class_index, data = read_u2(data)
        self.this_class = self.constants[this_class_index].msg
        print("This class:", self.this_class)

        super_class_index, data = read_u2(data)
        self.super_class = self.constants[super_class_index].msg
        print("Super:", self.super_class)

        self.interfaces, data = self._read_interfaces(data)
        print("Interfaces:", self.interfaces)

        self.fields_count, data = read_u2(data)
        self.fields = []

        print("field count =", self.fields_count)

        for _ in range(self.fields_count):
            field = Field(data, self.constant_pool)
            self.fields.append(field)
            data = field.data

        self.methods_count, data = read_u2(data)
        self.methods = []

        print("method count =", self.methods_count)

        for _ in range(self.methods_count):
            method = Method(data, self.constant_pool)
            self.methods.append(method)
            data = method.data

        print("Methods:", ",".join([mt.name for mt in self.methods]))

        self.attributes, data = self._read_attribs(data, self.constant_pool)


        print("Remaining data:", len(data))

    @staticmethod
    def _read_u4(data):
        """Reads a 4 byte data string"""
        return data[:4], data[4:]

    def _read_access_flags(self, data):
        """Returns access flags"""
        raw, data = read_u2(data)
        return AccessFlags(raw, "class"), data

    def _read_interfaces(self, data):
        count, data = read_u2(data)
        interfaces = []
        if count == 0:
            return [], data
        for _ in range(count):
            ref, data = read_u2(data)
            interfaces.append(self.constants[ref].msg)
        return interfaces

    def _read_attribs(self, data, pool):
        self.attrib_count, data = read_u2(data)
        print("Class attrib count", self.attrib_count)
        attrib = []
        for _ in range(self.attrib_count):
            a = Attribute(data, pool)
            data = a.data # use trimmed data
            self.data = data
            attrib.append(a)
        return attrib, data

    def get_methods(self):
        return self.methods

    def get_attributes(self):
        return self.attributes

    def get_fields(self):
        return self.fields
