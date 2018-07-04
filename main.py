import serial
serial = serial.Serial("/dev/whatever", 50000)
data = "Tight" + "\n"

print >> serial, len(data)
serial.write(data)