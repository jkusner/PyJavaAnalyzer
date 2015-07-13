class AccessFlags:
    ACC_PUBLIC = 0x0001
    ACC_PRIVATE = 0x0002 # <- for fields/methods only
    ACC_PROTECTED = 0x0004 # <- for fields/methods only
    ACC_STATIC = 0x008 # <- fields/methods only
    ACC_FINAL = 0x0010 # <- fields/methods only
    ACC_SYNCHRONIZED = 0x0020 # <- method only
    ACC_SUPER = 0x0020 # <- class only
    ACC_VOLATILE = 0x0040 # <- field
    ACC_BRIDGE = 0x0040 # <- method
    ACC_VARARGS = 0x0080 # <- method
    ACC_TRANSIENT = 0x0080 # <- field
    ACC_NATIVE = 0x0100 # method
    ACC_INTERFACE = 0x200
    ACC_ABSTRACT = 0x0400 # <- class, method
    ACC_STRICT = 0x0800 # method (strictfp)
    ACC_SYNTHETIC = 0x1000
    ACC_ANNOTATION = 0x2000 # <- class
    ACC_ENUM = 0x4000

    def __init__(self, short, ctype = "?"):
        self.flags = []
        self.raw = short
        self.msg = ""

        if short & AccessFlags.ACC_PUBLIC:
            self.flags.append("public")
        if short & AccessFlags.ACC_FINAL:
            self.flags.append("final")
        if short & AccessFlags.ACC_SUPER: # might be synchronized if method
            if ctype == "class":
                self.flags.append("super")
            else:
                self.flags.append("synchronized")
        if short & AccessFlags.ACC_INTERFACE:
            self.flags.append("interface")
        if short & AccessFlags.ACC_ABSTRACT:
            self.flags.append("abstract")
        if short & AccessFlags.ACC_SYNTHETIC:
            self.flags.append("synthetic")
        if short & AccessFlags.ACC_ANNOTATION:
            self.flags.append("annotation")
        if short & AccessFlags.ACC_PRIVATE:
            self.flags.append("private")
        if short & AccessFlags.ACC_PROTECTED:
            self.flags.append("protected")
        if short & AccessFlags.ACC_STATIC:
            self.flags.append("static")
        if short & AccessFlags.ACC_VOLATILE: # might be BRIDGE if method
            if ctype == "method":
                self.flags.append("bridge")
            else:
                self.flags.append("volatile")
        if short & AccessFlags.ACC_TRANSIENT: # might be varargs
            if ctype == "method":
                self.flags.append("varargs")
            else:
                self.flags.append("transient")
        if short & AccessFlags.ACC_ENUM:
            self.flags.append("enum")

        self.msg = " ".join(self.flags)
    def __str__(self):
        return "raw: " + str(self.raw) + ". (" + self.msg + ")"

