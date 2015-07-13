from .accessflags import AccessFlags
from .attribute import Attribute
from .util import *

class Method:
    def __init__(self, data, pool):
        raw_flags, data = read_u2(data)
        self.access_flags = AccessFlags(raw_flags, "method")

        self.name_index, data = read_u2(data)
        self.name = pool[self.name_index].msg

        self.descriptor_index, data = read_u2(data)
        self.descriptor = pool[self.descriptor_index].msg

        self.attributes, data = self._read_attribs(data, pool)

        self.data = data

    def _read_attribs(self, data, pool):
        self.attrib_count, data = read_u2(data)
        attrib = []
        for _ in range(self.attrib_count):
            a = Attribute(data, pool)
            data = a.data # use trimmed data
            self.data = data
            attrib.append(Attribute(data, pool))
        return attrib, data

    def get_name(self):
        return self.name

    def get_attributes(self):
        return self.attributes