import os
print("-----------------------")
print("| Qemu Starter Script |")
print("-----------------------")
config = input("Select configuration (macOS or other): ")
if (config == "macOS"):
    drive_c = input("Enter file patch to C Drive: ")
    drive_d_enabled = True
    drive_d = input("Enter file patch to D drive (or press enter to skip): ")
    if(drive_d == ""):
        drive_d_enabled = False
    memory = input('Enter RAM to MB: ')
    param = input("Enter custom parameters or press Enter: ")
    if(drive_d_enabled == True):
        os.system("qemu-system-ppc -L pc-bios -boot c -M mac99 -m " + memory + " -drive file=" + drive_d + ",format=raw,media=cdrom -drive file=" + drive_c + ",format=qcow2,media=disk " + param)
    if(drive_d_enabled == False):
        os.system("qemu-system-ppc -L pc-bios -boot c -M mac99 -m " + memory + " -drive file=" + drive_c + ",format=qcow2,media=disk " + param)
if (config == "other"):
    architecture_select = input("Select qemu package (qemu-system-i386 (x86 systems), qemu-system-ppc (PowerPC systems), qemu-system-arm (Arm systems)): ")
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