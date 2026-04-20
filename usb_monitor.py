import wmi
import time

def monitor_usb():
    c = wmi.WMI()
    print("Monitoring USB devices...")

    known = set()

    while True:
        current = set()

        for disk in c.Win32_DiskDrive():
            if "USB" in disk.InterfaceType:
                current.add(disk.Caption)

        new_devices = current - known
        removed_devices = known - current

        for device in new_devices:
            print(f"[+] USB Connected: {device}")

        for device in removed_devices:
            print(f"[-] USB Removed: {device}")

        known = current
        time.sleep(3)