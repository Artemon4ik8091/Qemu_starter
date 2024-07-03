import os
print("-----------------------")
print("| Qemu Starter Script |")
print("-----------------------")
start = True
while(start == True):
    mode = input("Select mode (1. Create virtual disk or 2. Start virtual machine) or enter exit to close script: ")
    if (mode == "Create virtual disk" or "1"):
        size = input("Enter size to disk (Gb): ")
        name = input("Enter name to disk: ")
        os.system("qemu-img create -f qcow2 " + name + ".qcow2 " + size + "G")
        print("Disk " + name + " created!")
    if (mode == "Start virtual machine" or "2"):
        config = input("Select configuration (1. macOS or 2. other): ")
        if (config == "macOS" or "1"):
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
        if (config == "other" or "2"):
            architecture_select = input("Select qemu package (1. qemu-system-i386 (x86 systems), 2. qemu-system-ppc (PowerPC systems), 3. qemu-system-arm (Arm systems)): ")
            if (architecture_select == "1"):
                architecture_select = "qemu-system-i386"
            if (architecture_select == "2"):
                architecture_select = "qemu-system-ppc"
            if (architecture_select == "1"):
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
    if(mode == "exit"):
        print("Closing...")
        start = False
