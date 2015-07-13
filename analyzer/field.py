from .accessflags import AccessFlags
from .attribute import Attribute
from .util import *

class Field:
    def __init__(self, data, pool):
        self.data = data
        self.pool = pool

        raw_flags, data = read_u2(data)
        self.flags = AccessFlags(raw_flags, "field")

        self.name_index, data = read_u2(data)

        self.name = pool[self.name_index].msg

        self.descriptor_index, data = read_u2(data)

        self.descriptor = pool[self.descriptor_index].msg

        print("Field[%s]: %s" % (self.name, self.descriptor))

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

