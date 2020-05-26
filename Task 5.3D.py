from gpiozero import LED
import RPi.GPIO as GPIO
from tkinter import *
import tkinter.font
import time
GPIO.setmode(GPIO.BCM)


LED = 18
GPIO.setup(LED, GPIO.OUT)


win = Tk()
win.title("Translate letter to morse code")
myFont = tkinter.font.Font(family ='Helverica', size=13, weight= "bold")


MORSE_CODE_DICT = { 'A':'.-',
                    'B':'-...', 
                    'C':'-.-.',
                    'D':'-..',
                    'E':'.', 
                    'F':'..-.',
                    'G':'--.',
                    'H':'....', 
                    'I':'..',
                    'J':'.---',
                    'K':'-.-', 
                    'L':'.-..',
                    'M':'--',
                    'N':'-.', 
                    'O':'---',
                    'P':'.--.',
                    'Q':'--.-', 
                    'R':'.-.',
                    'S':'...',
                    'T':'-', 
                    'U':'..-',
                    'V':'...-',
                    'W':'.--', 
                    'X':'-..-',
                    'Y':'-.--',
                    'Z':'--..', 
                    '1':'.----',
                    '2':'..---',
                    '3':'...--', 
                    '4':'....-',
                    '5':'.....',
                    '6':'-....', 
                    '7':'--...',
                    '8':'---..',
                    '9':'----.', 
                    '0':'-----',
                    ', ':'--..--',
                    '.':'.-.-.-', 
                    '?':'..--..',
                    '/':'-..-.',
                    '-':'-....-', 
                    '(':'-.--.',
                    ')':'-.--.-'}





def Dot():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.7)

    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.7)
    
    
def Dash():
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(2)



def Translate():

    input = user_input.get()
    for char in input:
        for char in MORSE_CODE_DICT[char.upper()]:
            if char != '.':
                Dash()
            elif char != '-':
                Dot()
            else:
                time.sleep(1)
        
        
        
user_input = Entry(win, font = myFont, width=17, bg= 'white')
user_input.grid(row=1, column=0)


btn = Button(win, text = 'Translate to morse code' ,font = myFont, command = Translate, bg= 'bisque2', height = 1, width = 18)
btn.grid(row=2, column=0)




