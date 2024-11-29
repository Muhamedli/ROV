import usb.core

devices = usb.core.find(find_all=True)

for device in devices:
    print("VID: {:04x}, PID: {:04x}".format(device.idVendor, device.idProduct))