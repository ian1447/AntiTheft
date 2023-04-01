import random
import speech_recognition as sr
import time
import serial
import RPi.GPIO as GPIO

#for speech to text
r = sr.Recognizer()
mic = sr.Microphone()

GPIO.setmode(GPIO.BOARD)  
#for arduino communication

port = serial.Serial("/dev/ttyUSB1", baudrate=115200, timeout = 1)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

global mywordlist
global mynumberlist
global pass_word_list
global pass_number_list
global DataisSent

DataisSent = False;

pass_word_list = []
pass_number_list = ""

mywordlist = ["table", "chair", "computer", "phone", "car", "black", "door", "window","hot", "keyboard", "wire", "light", "water", "notebook", "shoes", "paper",
              "camera", "sound", "lock", "screen", "bed", "talk", "run", "bag"]

mynumberlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def create_random():
    global pass_word_list
    global pass_number_list
    
    pass_word_list = []
    for i in range(4):
        pass_word_list.append(random.choice(mywordlist))

    pass_number_list = ""
    for i in range(6):
        pass_number_list = pass_number_list+(random.choice(mynumberlist))

#while True:
#    print("Enter [1] for Speech")
#    print("Enter [2] for Code")
#    choice = input("Enter Choice: ")
#    if choice == "1" or choice == "2":
#    break



choice = ""
while True:
    create_random()
    if choice == "":
        if (DataisSent == False):
                    
            time.sleep(1)
            port.write(b'AT\r\n')
            time.sleep(1)

            port.write(b'AT+CFUN=1\r\n')
            time.sleep(2)

            port.write(b'AT+CMGF=1\r\n')
            time.sleep(2)

            #port.write(b'AT+CNMI=2,1,0,0,0\r\n')
            #time.sleep(2)
            #rcv = port.read(50)
            #print(rcv)

            port.write(b'AT+CMGS="09951053257"\r\n')
            time.sleep(2)

            msg = "helloaasdasd"
            port.reset_output_buffer()
            time.sleep(1)
            port.write(str.encode(msg + chr(26)))
            time.sleep(2)
            time.sleep(3)
            print("Sending Data...")
            ser.write(b"c\n")
            print("Waiting For Data")
            DataisSent = True
        time.sleep(8)
        if ser.in_waiting > 0:
            choice = ser.readline().decode('utf-8').rstrip()
            print(choice)
    
    if choice == "A":
        count = 0
        time.sleep(3)
        while count != 4:
            print(pass_word_list[count])
            ser.write(str(pass_word_list[count]).encode('utf-8'))
            count += 1
            time.sleep(3)
            
        print(pass_word_list)
        counter = 0
        wrong_counter = 0
        while counter < 4:
            with mic as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout = 10.0)
                try:            
                    word = r.recognize(audio)
                    if (word == pass_word_list[counter]):
                        counter += 1
                        print("Correct next")
                    else:
                        wrong_counter += 1
                        print("Try Again")
                except LookupError:
                    wrong_counter += 1
                    print("Try Again")
            if wrong_counter == 5:
                break


        if wrong_counter == 5:
            print("Wrong Password Given!!")
            choice = ""
        else:
            print("Unlocked!")
            time.sleep(2)
            ser.write(b"u\n")
            time.sleep(2)
            choice = ""
            DataisSent = False

    elif choice == "B":
        time.sleep(3)
        counter = 0
        print(pass_number_list)
        ser.write(str(pass_number_list).encode('utf-8'))
        time.sleep(2)
        while counter < 4:
            if ser.in_waiting > 0:
                result = ser.readline().decode('utf-8').rstrip()
                counter = counter + 1
                #password = input("Enter Password: ")
                if result == "Y":
                    time.sleep(2)
                    ser.write(b"u\n")
                    print("Unlocked")
                    DataisSent = False
                    time.sleep(2)
                    choice = ""
                    break
                else:
                    print("Try Again")

            if counter == 3:
                print("Run out of tries")
                choice = ""
                DataisSent = False
                break