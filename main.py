import serial
time.sleep(5)
serial = serial.Serial("/dev/whatever", 50000)
data = "Tight" + "\n"

print >> serial, len(data)
serial.write(data)
time.sleep(5)