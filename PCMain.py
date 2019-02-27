import serial
import time
print("Test1!")
#time.sleep(2)
print("Test1.5!")
myserial = serial.UART(                           #("/dev/whatever", 50000)
data = int(1) #"Tight" + "\n"
loop = 0

#print >> myserial, len(data)
myserial.write(data)
while loop < 1000:
    myserial.write(1) #(data)
    if loop % 10 == 0:
        print(loop)
    loop += 1
#time.sleep(2)
print("Test2!")
time.sleep(3)