import os

size = input("Enter size to disk (Gb): ")
name = input("Enter name to disk: ")
os.system("qemu-img create -f qcow2 " + name + ".qcow2 " + size + "G")
print("Disk " + name + " created!")