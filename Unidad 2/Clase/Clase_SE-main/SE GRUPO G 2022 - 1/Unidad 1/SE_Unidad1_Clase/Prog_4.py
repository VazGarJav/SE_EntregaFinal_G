import serial as connector

arduino = connector.Serial("com2", baudrate=9600, timeout=1)


arduino.write("2".encode())


arduino.close()
