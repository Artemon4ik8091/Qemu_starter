import os

architecture_select = input("Select qemu package (1. qemu-system-i386 (x86 systems), 2. qemu-system-ppc (PowerPC systems), 3. qemu-system-arm (Arm systems)): ")
if (architecture_select == "1"):
    architecture_select = "qemu-system-i386"
if (architecture_select == "2"):
    architecture_select = "qemu-system-ppc"
if (architecture_select == "3"):
    architecture_select = "qemu-system-arm"
drive_c = input("Enter file patch to C Drive: ")
drive_d_enabled = True
drive_d = input("Enter file patch to D drive (or press enter to skip): ")
if(drive_d == ""):
    drive_d_enabled = False
memory = input('Enter RAM to MB: ')
boot_select = input("Enter disk to boot (c or d): ")
param = input("Enter custom parameters or press Enter: ")
print("Starting " + architecture_select + "...")
if(drive_d_enabled == True):
    os.system(architecture_select + " -boot " + boot_select + " -m " + memory + " -drive file=" + drive_d + ",format=raw,media=cdrom -drive file=" + drive_c + ",format=qcow2,media=disk " + param)
if(drive_d_enabled == False):
    os.system(architecture_select + " -boot " + boot_select + " -m " + memory + " -drive file=" + drive_c + ",format=qcow2,media=disk " + param)
