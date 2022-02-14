import bluetooth

#bDetect all Bluetooth devices and Create an array with all the MAC addresses
print("Searching for devices...")
nearby_devices = bluetooth.discover_devices(lookup_names=True)

#Run through all the devices found and list their name
print("Select your device by entering its coresponding number...")
for i in nearby_devices:
    num+=1
    print(str(num) + ": " + bluetooth.lookup_name( i ))
   
#Allow the user to select their Arduino
selection = int(input("> ")) - 1
bd_addr = nearby_devices[selection]
port = 1

print("You have selected " + bluetooth.lookup_name(nearby_devices[selection]))

# Connect to bluetooth address and port
sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

data = "L"
sock.send(data)

data = "Z"
sock.send(data)

data = sock.recv(1024)
print(data)
# Print out appearsto be those of Serial.println and not bluetooth.println
   
sock.getsockname()
sock.getpeername()

sock.close()