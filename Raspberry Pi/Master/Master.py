'''
R2-----------------------R3
|                        |    
|                        |
|                        | 
|         (Exit)         |
R1----------R5-----------R4
'''

import pymysql
import serial
import schedule
import time
import socket
import sys
import unicodedata
import numpy as np
from numpy.polynomial import polynomial as P
from redis.exceptions import TimeoutError
import math

c=-63
m=-40.916

#DIMENSION LENGTH WIDTH (METERS)
x=2
y=5
h=3

#Distance between exit and Receiver1
a=1
#Distance between exit and Receiver4
b=1

x1=0
x2=0
x3=x 
x4=x
x5=a

y1=0
y2=y
y3=y
y4=0 
y5=0

#RSSI calculation
α = -2.0458
d0 = 0.113626471

#Receiver1
UDP_IP1 = "192.168.216.43"
UDP_PORT1 = 2390
MESSAGE = b"Hello, World!"

#Receiver2
UDP_IP2 = "192.168.216.233"
UDP_PORT2 = 2393
MESSAGE = b"Hello, World!"

#Receiver3
UDP_IP3 = "192.168.216.3"
UDP_PORT3 = 2391
MESSAGE = b"Hello, World!"

#Receiver4
UDP_IP4 = "192.168.216.250"
UDP_PORT4 = 2392
MESSAGE = b"Hello, World!"

#Receiver5
UDP_IP5 = "192.168.216.143"
UDP_PORT5 = 2394
MESSAGE = b"Hello, World!"


#Receiver1
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP1, UDP_PORT1))

#Receiver2
sock2 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock2.sendto(MESSAGE, (UDP_IP2, UDP_PORT2))

#Receiver3
sock3 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock3.sendto(MESSAGE, (UDP_IP3, UDP_PORT3))

#Receiver4
sock4 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock4.sendto(MESSAGE, (UDP_IP4, UDP_PORT4))

#Receiver5
sock5 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock5.sendto(MESSAGE, (UDP_IP5, UDP_PORT5))

RSSI1 = 0
RSSI2 = 0
RSSI3 = 0
RSSI4 = 0
RSSI5 = 0
    
class NoFeatures(Exception):
    pass

def Receiver1():
    global R1Transmitter, R1value, RSSI1
    #Receiver1:
    Receiver1, server = sock.recvfrom(4096)
    Receiver1 = Receiver1.decode('utf-8').rstrip()
    R1Transmitter = Receiver1[0]
    RSSI1 = Receiver1[2:8]
    RSSI1 = (int(RSSI1))

def Receiver2():
    global R2Transmitter, R2value, RSSI2
    #Receiver2:
    Receiver2, server = sock2.recvfrom(4096)
    Receiver2 = Receiver2.decode('utf-8').rstrip()
    R2Transmitter = Receiver2[0]
    RSSI2 = Receiver2[2:8]
    RSSI2 = (int(RSSI2))
    
def Receiver3():
    global R3Transmitter, R3value, RSSI3
    #Receiver3:
    Receiver3, server = sock3.recvfrom(4096)
    Receiver3 = Receiver3.decode('utf-8').rstrip()
    R3Transmitter = Receiver3[0]
    RSSI3 = Receiver3[2:8]
    RSSI3 = (int(RSSI3))
    
def Receiver4():
    global R4Transmitter, R4value, RSSI4
    #Receiver4:
    Receiver4, server = sock4.recvfrom(4096)
    Receiver4 = Receiver4.decode('utf-8').rstrip()
    R4Transmitter = Receiver4[0]
    RSSI4 = Receiver4[2:8]
    RSSI4 = (int(RSSI4))
    
def Receiver5():
    global R5Transmitter, R5value, RSSI5
    #Receiver5:
    Receiver5, server = sock5.recvfrom(4096)
    Receiver5 = Receiver5.decode('utf-8').rstrip()
    R5Transmitter = Receiver5[0]
    RSSI5 = Receiver5[2:8]
    RSSI5 = (int(RSSI5))
    
def GetCoordinate(RSSI1, RSSI2, RSSI3, RSSI4, RSSI5):
    print(RSSI1, RSSI2, RSSI3, RSSI4, RSSI5)
    global xt, yt, d5
    
    #y=mx+c
    #RSSI=-40.916(logd)-38.646
    #(RSSI+c)/-40.916=logd
    #ln((RSSI+c)/-40.916)=d
    
    d1=10**((RSSI1-c)/m)
    d2=10**((RSSI2-c)/m)
    d3=10**((RSSI3-c)/m)
    d4=10**((RSSI4-c)/m)
    d5=10**((RSSI5-c)/m)
    #print(d1,d2,d3,d4,d5)
    '''
    #d1
    d1 = 10**((RSSI1 + 20*α*math.log(d0,10))/(20*α))
    #d1 = math.sqrt(d1**2-(h-1.5)**2)
    
    #d2
    d2 = 10**((RSSI2 + 20*α*math.log(d0,10))/(20*α))
    #d2 = math.sqrt(d2**2-(h-1.5)**2)
    
    #d3
    d3 = 10**((RSSI3 + 20*α*math.log(d0,10))/(20*α))
    #d3 = math.sqrt(d3**2-(h-1.5)**2)
    
    #d4
    d4 = 10**((RSSI4 + 20*α*math.log(d0,10))/(20*α))
    #d4 = math.sqrt(d4**2-(h-1.5)**2)
    
    #d5
    d5 = 10**((RSSI5 + 20*α*math.log(d0,10))/(20*α))
    #d5 = math.sqrt(d5**2-(h-1.5)**2)
    #print(d1,d2,d3,d4,d5)
    '''
    #d
    d1=d1**2-x1**2-y1**2
    d2=d2**2-x2**2-y2**2
    d3=d3**2-x3**2-y3**2
    d4=d4**2-x4**2-y4**2
    d5=d5**2-x5**2-y5**2
    
    #R1,2,3
    A1 = np.array([[-2*x1, -2*y1, 1],
                 [-2*x2, -2*y2, 1],
                 [-2*x3, -2*y3, 1]])
    B1 = np.array([d1, d2, d3])
    A1i=(np.linalg.inv(A1))
    xs1=np.dot(A1i, B1)
    #[xt,yt,(xt**2+yt**2)]
    #print(xs1)
    
    #R2,3,4
    A2 = np.array([[-2*x2, -2*y2, 1],
                 [-2*x3, -2*y3, 1],
                 [-2*x4, -2*y4, 1]])
    B2 = np.array([d2, d3, d4])
    A2i=(np.linalg.inv(A2))
    xs2=np.dot(A2i, B2)
    #[xt,yt,(xt**2+yt**2)]
    #print(xs2)
    
    #R1,3,4
    A3 = np.array([[-2*x1, -2*y1, 1],
                 [-2*x3, -2*y3, 1],
                 [-2*x4, -2*y4, 1]])
    B3 = np.array([d1, d3, d4])
    A3i=(np.linalg.inv(A3))
    xs3=np.dot(A3i, B3)
    #[xt,yt,(xt**2+yt**2)]
    #print(xs3)
    
    #R1,2,4
    A4= np.array([[-2*x1, -2*y1, 1],
                 [-2*x2, -2*y2, 1],
                 [-2*x4, -2*y4, 1]])
    B4 = np.array([d1, d2, d4])
    A4i=(np.linalg.inv(A4))
    xs4=np.dot(A4i, B4)
    #[xt,yt,(xt**2+yt**2)]
    #print(xs4)
    
    #R3,2,5
    A5 = np.array([[-2*x3, -2*y3, 1],
                 [-2*x2, -2*y2, 1],
                 [-2*x5, -2*y5, 1]])
    B5 = np.array([d3, d2, d5])
    A5i=(np.linalg.inv(A5))
    xs5=np.dot(A5i, B5)
    #[xt,yt,(xt**2+yt**2)]
    #print(xs5)
    
    #R1,2,5
    A6 = np.array([[-2*x1, -2*y1, 1],
                 [-2*x2, -2*y2, 1],
                 [-2*x5, -2*y5, 1]])
    B6 = np.array([d1, d2, d5])
    A6i=(np.linalg.inv(A6))
    xs6=np.dot(A6i, B6)
    #[xt,yt,(xt**2+yt**2)]
    #print(xs6)
    
    #R3,4,5
    A7 = np.array([[-2*x3, -2*y3, 1],
                 [-2*x4, -2*y4, 1],
                 [-2*x5, -2*y5, 1]])
    B7 = np.array([d3, d4, d5])
    A7i=(np.linalg.inv(A7))
    xs7=np.dot(A7i, B7)
    #[xt,yt,(xt**2+yt**2)]
    #print(xs7)
    
    #R1,3,5
    A8 = np.array([[-2*x1, -2*y1, 1],
                 [-2*x3, -2*y3, 1],
                 [-2*x5, -2*y5, 1]])
    B8 = np.array([d1, d3, d5])
    A8i=(np.linalg.inv(A8))
    xs8=np.dot(A8i, B8)
    #[xt,yt,(xt**2+yt**2)]
    #print(xs8)
    
    #R2,4,5
    A9 = np.array([[-2*x2, -2*y2, 1],
                 [-2*x4, -2*y4, 1],
                 [-2*x5, -2*y5, 1]])
    B9 = np.array([d2, d4, d5])
    A9i=(np.linalg.inv(A9))
    xs9=np.dot(A9i, B9)
    #[xt,yt,(xt**2+yt**2)]
    #print(xs9)
    
    xt=(xs1[0]+xs2[0]+xs3[0]+xs4[0]+xs5[0]+xs6[0]+xs7[0]+xs8[0]+xs9[0])/9
    yt=(xs1[1]+xs2[1]+xs3[1]+xs4[1]+xs5[1]+xs6[1]+xs7[1]+xs8[1]+xs9[1])/9
    #xt=(xs1[0]+xs2[0]+xs3[0]+xs4[0])/4
    #yt=(xs1[1]+xs2[1]+xs3[1]+xs4[1])/4

#---------------------------------------------------------Transmitter1---------------------------------------------------------#
def R1Transmitter1():
    Receiver1()
    """
    if R1Transmitter == '1':
        print("Receiver1: 192.168.20.98",RSSI1)
    else:
        raise NoFeatures(RSSI1)
    """
def R2Transmitter1():
    Receiver2()
    """
    if R2Transmitter == '1':
        print("Receiver2: 192.168.20.51",RSSI2)
    else:
        raise NoFeatures(RSSI2)
    """
def R3Transmitter1():
    Receiver3()
    """
    if R3Transmitter == '1':
        print("Receiver3: 192.168.20.43",RSSI3)
    else:
        raise NoFeatures(RSSI3)
    """
def R4Transmitter1():
    Receiver4()
    """"
    if R4Transmitter == '1':
        print("Receiver4: 192.168.20.250",RSSI4)
    else:
        raise NoFeatures(RSSI4)
    """
def R5Transmitter1():
    Receiver5()
    """
    if R5Transmitter == '1':
        print("Receiver5: 192.168.20.143",RSSI5)
    else:
        raise NoFeatures(RSSI5)
    """
def Transmitter1():
    #print("Transmitter1")              
    attempts = 10
    """
    R1Transmitter1()
    R2Transmitter1()
    R3Transmitter1()
    R4Transmitter1()
    R5Transmitter1()
    """
    while attempts:
        try:
            R1Transmitter1()
            #print(RSSI1)
            break
        except NoFeatures:
            attempts -= 1
            print("Retry",attempts)
            
    if attempts != 0:
        attempts = 10
        while attempts:
            try:
                R2Transmitter1()
                #print(RSSI2)
                break
            except NoFeatures:
                attempts -= 1
                print("Retry",attempts)
                
        attempts = 10
        while attempts:
            try:
                R3Transmitter1()
                #print(RSSI3)
                break
            except NoFeatures:
                attempts -= 1
                print("Retry",attempts)
                
        attempts = 10
        while attempts:
            try:
                R4Transmitter1()
                #print(RSSI4)
                break
            except NoFeatures:
                attempts -= 1
                print("Retry",attempts)
                
        attempts = 10
        while attempts:
            try:
                R5Transmitter1()
                #print(RSSI5)
                break
            except NoFeatures:
                attempts -= 1
                print("Retry",attempts)
    
    GetCoordinate(RSSI1, RSSI2, RSSI3, RSSI4, RSSI5)
    #print(xt,yt)
    if(RSSI1!=0 and RSSI2!=0 and RSSI3!=0 and RSSI4!=0 and RSSI5!=0):    
        
        #TARGET 1 Inside
        if(xt>=0 and xt<=x and yt>=0 and yt<=y):
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Inside' WHERE LoRaNo = '101';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            #print("TARGET 1")
            #print("Inside")
            
        #TARGET 1 Escape Direction A (Left)
        elif yt<0 and xt>a:
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '101';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            #print("TARGET 1")
            #print("Direction A: Escape to Left")
            #print("Distance between Patient and Exit: ", d5, "m")
            #print("Escape to Left")
            #print("Escape to Left",float(90-np.arccos(-(d11**2-a**2-d51**2)/(2*a*d51))*180/math.pi),"degrees")
            
        #TARGET 1 Escape Direction A (Right)
        elif yt<0 and xt<(x-b):
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '101';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            #print("TARGET 1")
            #print("Direction A: Escape to Right") 
            #print("Distance between Patient and Exit: ", d5, "m")
            #print("Escape to Right")
            #print("Escape to Right",float(90-np.arccos(-(d41**2-b**2-d51**2)/(2*b*d51))*180/math.pi), "degrees")
            
        #TARGET 1 Escape Direction B
        elif xt<0:
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '101';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            #print("TARGET 1")
            #print("Escape to Direction B")
            #print("Distance between Patient and Exit: ", d5, "m")
            
        #TARGET 1 Escape Direction C
        elif yt>y:
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '101';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            #print("TARGET 1")
            #print("Escape to Direction C")
            #print("Distance between Patient and Exit: ", d5, "m")
    
        #TARGET 1 Escape Direction D
        elif xt>x:
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '101';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            #print("TARGET 1")
            #print("Escape to Direction D")
            #print("Distance between Patient and Exit: ", d5, "m")
        
        #TARGET 1 LOCATION    
        #print("Patient Location:")
        print(xt,yt)
        #print("")
        
    else:
        connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
        cursor = connection.cursor()
        
        # queries for Update values
        updateSql = "UPDATE LoRa SET State = 'Off' WHERE LoRaNo = '101';"
        cursor.execute(updateSql)
    
        #commiting the connection then closing it.
        connection.commit()
        connection.close()
        print("No Transmitter 1")
        print("")

#---------------------------------------------------------Transmitter2---------------------------------------------------------#
def R1Transmitter2():
    Receiver1()
    if R1Transmitter == '2':
        print("Receiver1: 192.168.20.98",RSSI1)
    else:
        raise NoFeatures(RSSI1)
    
def R2Transmitter2():
    Receiver2()
    if R2Transmitter == '2':
        print("Receiver2: 192.168.20.51",RSSI2)
    else:
        raise NoFeatures(RSSI2)
    
def R3Transmitter2():
    Receiver3()
    if R3Transmitter == '2':
        print("Receiver3: 192.168.20.43",RSSI3)
    else:
        raise NoFeatures(RSSI3)
    
def R4Transmitter2():
    Receiver4()
    if R4Transmitter == '2':
        print("Receiver4: 192.168.20.250",RSSI4)
    else:
        raise NoFeatures(RSSI4)
    
def R5Transmitter2():
    Receiver5()
    if R5Transmitter == '2':
        print("Receiver5: 192.168.20.143",RSSI5)
    else:
        raise NoFeatures(RSSI5)

def Transmitter2():
    print("Transmitter2")              
    attempts = 10
    while attempts:
        try:
            R1Transmitter2()
            #print(RSSI1)
            break
        except NoFeatures:
            attempts -= 1
            print("Retry",attempts)
    
    if attempts != 0:
        attempts = 10
        while attempts:
            try:
                R2Transmitter2()
                #print(RSSI2)
                break
            except NoFeatures:
                attempts -= 1
                print("Retry",attempts)
                
        attempts = 10
        while attempts:
            try:
                R3Transmitter2()
                #print(RSSI3)
                break
            except NoFeatures:
                attempts -= 1
                print("Retry",attempts)
                
        attempts = 10
        while attempts:
            try:
                R4Transmitter2()
                #print(RSSI4)
                break
            except NoFeatures:
                attempts -= 1
                print("Retry",attempts)
                
        attempts = 10
        while attempts:
            try:
                R5Transmitter2()
                #print(RSSI5)
                break
            except NoFeatures:
                attempts -= 1
                print("Retry",attempts)
        
        
    GetCoordinate(RSSI1, RSSI2, RSSI3, RSSI4, RSSI5)
    print(xt,yt)
    if(attempts!=0 and RSSI2!=0 and RSSI3!=0 and RSSI4!=0 and RSSI5!=0):    
        #TARGET 2 Inside
        if(xt>=0 and xt<=x and yt>=0 and yt<=y):
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Inside' WHERE LoRaNo = '102';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            print("TARGET 2")
            print("Inside")
            
        #TARGET 2 Escape Direction A (Left)
        elif yt<0 and xt>a:
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '102';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            print("TARGET 2")
            print("Direction A: Escape to Left")
            print("Distance between Patient and Exit: ", d5, "m")
            print("Escape to Left")
            #print("Escape to Left",float(90-np.arccos(-(d11**2-a**2-d51**2)/(2*a*d51))*180/math.pi),"degrees")
            
        #TARGET 2 Escape Direction A (Right)
        elif yt<0 and xt<(x-b):
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '102';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            print("TARGET 2")
            print("Direction A: Escape to Right") 
            print("Distance between Patient and Exit: ", d5, "m")
            print("Escape to Right")
            #print("Escape to Right",float(90-np.arccos(-(d41**2-b**2-d51**2)/(2*b*d51))*180/math.pi), "degrees")
            
        #TARGET 2 Escape Direction B
        elif xt<0:
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '102';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            print("TARGET 2")
            print("Escape to Direction B")
            print("Distance between Patient and Exit: ", d5, "m")
            
        #TARGET 2 Escape Direction C
        elif yt>y:
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '102';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            print("TARGET 2")
            print("Escape to Direction C")
            print("Distance between Patient and Exit: ", d5, "m")
    
        #TARGET 2 Escape Direction D
        elif xt>x:
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '102';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            print("TARGET 2")
            print("Escape to Direction D")
            print("Distance between Patient and Exit: ", d5, "m")
        
        #TARGET 2 LOCATION    
        print("Patient Location:")
        print(xt,yt)
        print("")
        
    else:
        connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
        cursor = connection.cursor()
        
        # queries for Update values
        updateSql = "UPDATE LoRa SET State = 'Off' WHERE LoRaNo = '102';"
        cursor.execute(updateSql)
    
        #commiting the connection then closing it.
        connection.commit()
        connection.close()
        print("No Transmitter 2")
        print("")



#---------------------------------------------------------Transmitter3---------------------------------------------------------#
def R1Transmitter3():
    Receiver1()
    if R1Transmitter == '3':
        print("Receiver1: 192.168.20.98",RSSI1)
    else:
        raise NoFeatures(RSSI1)
    
def R2Transmitter3():
    Receiver2()
    if R2Transmitter == '3':
        print("Receiver2: 192.168.20.51",RSSI2)
    else:
        raise NoFeatures(RSSI2)
    
def R3Transmitter3():
    Receiver3()
    if R3Transmitter == '3':
        print("Receiver3: 192.168.20.43",RSSI3)
    else:
        raise NoFeatures(RSSI3)
    
def R4Transmitter3():
    Receiver4()
    if R4Transmitter == '3':
        print("Receiver4: 192.168.20.250",RSSI4)
    else:
        raise NoFeatures(RSSI4)
    
def R5Transmitter3():
    Receiver5()
    if R5Transmitter == '3':
        print("Receiver5: 192.168.20.143",RSSI5)
    else:
        raise NoFeatures(RSSI5)

def Transmitter3():
    print("Transmitter3")              
    attempts = 10
    while attempts:
        try:
            R1Transmitter3()
            #print(RSSI1)
            break
        except NoFeatures:
            attempts -= 1
            print("Retry",attempts)
    
    if attempts != 0:
        attempts = 10
        while attempts:
            try:
                R2Transmitter3()
                #print(RSSI2)
                break
            except NoFeatures:
                attempts -= 1
                print("Retry",attempts)
                
        attempts = 10
        while attempts:
            try:
                R3Transmitter3()
                #print(RSSI3)
                break
            except NoFeatures:
                attempts -= 1
                print("Retry",attempts)
                
        attempts = 10
        while attempts:
            try:
                R4Transmitter3()
                #print(RSSI4)
                break
            except NoFeatures:
                attempts -= 1
                print("Retry",attempts)
                
        attempts = 10
        while attempts:
            try:
                R5Transmitter3()
                #print(RSSI5)
                break
            except NoFeatures:
                attempts -= 1
                print("Retry",attempts)
        
        
    GetCoordinate(RSSI1, RSSI2, RSSI3, RSSI4, RSSI5)
    print(xt,yt)
    if(attempts!=0 and RSSI2!=0 and RSSI3!=0 and RSSI4!=0 and RSSI5!=0):    
        #TARGET 3 Inside
        if(xt>=0 and xt<=x and yt>=0 and yt<=y):
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Inside' WHERE LoRaNo = '103';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            print("TARGET 3")
            print("Inside")
            
        #TARGET 3 Escape Direction A (Left)
        elif yt<0 and xt>a:
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '103';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            print("TARGET 3")
            print("Direction A: Escape to Left")
            print("Distance between Patient and Exit: ", d5, "m")
            print("Escape to Left")
            #print("Escape to Left",float(90-np.arccos(-(d11**2-a**2-d51**2)/(2*a*d51))*180/math.pi),"degrees")
            
        #TARGET 3 Escape Direction A (Right)
        elif yt<0 and xt<(x-b):
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '103';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            print("TARGET 3")
            print("Direction A: Escape to Right") 
            print("Distance between Patient and Exit: ", d5, "m")
            print("Escape to Right")
            #print("Escape to Right",float(90-np.arccos(-(d41**2-b**2-d51**2)/(2*b*d51))*180/math.pi), "degrees")
            
        #TARGET 3 Escape Direction B
        elif xt<0:
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '103';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            print("TARGET 3")
            print("Escape to Direction B")
            print("Distance between Patient and Exit: ", d5, "m")
            
        #TARGET 3 Escape Direction C
        elif yt>y:
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '103';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            print("TARGET 3")
            print("Escape to Direction C")
            print("Distance between Patient and Exit: ", d5, "m")
    
        #TARGET 3 Escape Direction D
        elif xt>x:
            connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
            cursor = connection.cursor()
            
            # queries for Update values
            updateSql = "UPDATE LoRa SET State = 'On' , Position = 'Outside' WHERE LoRaNo = '103';"
            cursor.execute(updateSql)
        
            #commiting the connection then closing it.
            connection.commit()
            connection.close()
            print("TARGET 3")
            print("Escape to Direction D")
            print("Distance between Patient and Exit: ", d5, "m")
        
        #TARGET 3 LOCATION    
        print("Patient Location:")
        print(xt,yt)
        print("")
        
    else:
        connection = pymysql.connect(host="localhost", user="pi", passwd="root", database="mydb")
        cursor = connection.cursor()
        
        # queries for Update values
        updateSql = "UPDATE LoRa SET State = 'Off' WHERE LoRaNo = '103';"
        cursor.execute(updateSql)
    
        #commiting the connection then closing it.
        connection.commit()
        connection.close()
        print("No Transmitter 3")
        print("")
        
schedule.every().seconds.do(Transmitter1)
schedule.every().seconds.do(Transmitter2)
schedule.every().seconds.do(Transmitter3)
            
while True:
    schedule.run_all()
