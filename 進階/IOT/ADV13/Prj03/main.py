from machine import UART
from time import sleep

uart = UART(1, baudrate=9600)
uart.init(9600, bits=8, parity=None, stop=1)

buf1 = bytearray(5)
buf1[0] = 0xAA
buf1[1] = 0x13
buf1[2] = 0x01
buf1[3] = 0x7F
buf1[4] = buf1[0] + buf1[1] + buf1[2] + buf1[3]
uart.write(buf1)

buf = bytearray(6)
buf[0] = 0xAA
buf[1] = 0x7
buf[2] = 0x2
buf[3] = 0x0
buf[4] = 0x47
buf[5] = buf[0] + buf[1] + buf[2] + buf[3] + buf[4]
uart.write(buf)
sleep(3)

buf2 = bytearray(4)
buf2[0] = 0xAA
buf2[1] = 0x04
buf2[2] = 0x00
buf2[3] = 0xAE
buf2[4] = buf2[0] + buf2[1] + buf2[2] + buf2[3]
uart.write(buf2)