import RPi.GPIO as GPIO
import time
import signal
import socket
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(7,GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(15,GPIO.IN)

TCP_IP = '10.0.0.118'
print("enter port number")
TCP_PORT = input()
BUFFER_SIZE = 1024
#MESSAGE = "Hello, World!"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#data = s.recv(BUFFER_SIZE)

connected_pins = [3,5,7,11,13,15]
print str(connected_pins)
#function checks all previos sensors
def check_prev (curr_position):
        for x in range(0, curr_position):
                #print "for loop " + str(x)
                if  GPIO.input( connected_pins [x] ):
                        return x+1

        return -1


#counter to keep track of inner nested if's
error = -1
counter_sens = 0
#error message returned after checking previous sensors
try :
        while(1):

                counter_sens = 0
                if not GPIO.input(3):
                        s.send("Filling Initiated {process step --> "+str(counter_sens)+ " }")
                        print("Filling Initiated {process step --> "+str(counter_sens)+ " }")
                        time.sleep(1)
                        counter_sens = 1



                if not GPIO.input(5):
                        counter_sens = 1
                        s.send("Bottle is in filler  {process step --> "+str(counter_sens)+ " }")
                        print("Bottle is in filler  {process step --> "+str(counter_sens)+ " }")
                        time.sleep(1)
                        error = check_prev(counter_sens)
                        if error != -1:
                                print "error 2"
                                break
                        counter_sens = 2

                if not GPIO.input(7):
                        counter_sens = 2
                        s.send("Caping is underway  {process step --> "+str(counter_sens)+ " }")
                        print("Caping is underway  {process step --> "+str(counter_sens)+ " }")
                        time.sleep(1)
                        error = check_prev(counter_sens)
                        if error != -1:
                                print"error 3"
                                break
                        counter_sens = 3

                if not GPIO.input(11):
                        counter_sens = 3
                        s.send("Bottle is being labeled {process step --> "+str(counter_sens)+ " }")
                        print("Bottle is being labeled {process step --> "+str(counter_sens)+ " }")
                        time.sleep(1)
                        error = check_prev(counter_sens)
                        if error != -1:
                                print"error 4"
                                break
                        counter_sens = 4

                if not GPIO.input(13):
                        counter_sens = 4
                        s.send("Filling Initiated {process step --> "+str(counter_sens)+ " }")
                        print("Filling Initiated {process step --> "+str(counter_sens)+ " }")
                        time.sleep(1)
                        error = check_prev(counter_sens)
                        if error != -1:
                                print"error 5"
                                break
                        counter_sens = 5

                if not GPIO.input(15):
                        counter_sens = 5
                        s.send("Batch is ready {process step --> "+str(counter_sens)+ " }")
                        print("Batch is ready {process step --> "+str(counter_sens)+ " }")
                        time.sleep(1)
                        error = check_prev(counter_sens)
                        if error != -1:
                                print "error 6"
                                break


        print ("error on sensor { " + str(error) + " } process halted " )
        s.send("error on sensor { " + str(error) + " } process halted " )
        s.close()

except KeyboardInterrupt :

        GPIO.cleanup()



