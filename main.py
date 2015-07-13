from analyzer.classfile import ClassFile



data = b""
with open(input("Class file location > "), "rb") as f:
    data = f.read()

cf = ClassFile(data)

methods = cf.get_methods()

for m in methods:
    print("Method:", m.name)
    print("\tAttributes:")
    for a in m.get_attributes():
        print("\t\t",a.name)