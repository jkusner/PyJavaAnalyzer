from .util import *

class Attribute:
    def __init__(self, data, pool):
        self.name_index, data = read_u2(data)
        self.name = pool[self.name_index].msg

        bites, data = read_u4(data)

        self.info = data[:bites]

        self.data = data[bites:]

        # print("Attrib[%s->%s]: %s" % (self.name_index, self.name, self.info))
