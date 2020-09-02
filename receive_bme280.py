#coding: utf-8
import time
import datetime
import serial

def readData():
    ser = serial.Serial("/dev/ttyAMA0", 115200, timeout=60)
    line = ser.readline().decode('utf-8')
    list1 = line.split(":")
    datetime_now = datetime.datetime.now().strftime("%H:%M:%S")
    temp = str(int(list1[10].lstrip("tm="))/100)
    humd = str(int(list1[11].lstrip("hu="))/100)
    pres = list1[12].lstrip("at=").rstrip()
           
    print(datetime_now)
    print("Temp.= " + temp + "deg.C")
    print("Humid.= " + humd + "%RH")
    print("Press.= " + pres + "hPa")

    ser.close()
    
    return temp, pres, humd

if __name__ == '__main__':
    try:
        readData()
    except KeyboardInterrupt:
        pass
    