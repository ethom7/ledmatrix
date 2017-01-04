"""
        lightrowstest.py
        
        Program is to drive the 16 pin 8x8 led matrix using WiringPi and Python.
        This will turn on all the led's by turning on the row pins.
        
        
        by Evan Thompson
        January 3, 2017
        
        https://github.com/ethom7/ledmatrix

        Pin Wiring

        WiringPi                Rpi             PORT             LED PIN
        0                       BCM 17          11              1
        1                       BCM 18          12              2
        2                       BCM 27          13              3
        3                       BCM 22          15              4
        4                       BCM 23          16              5
        5                       BCM 24          18              6
        6                       BCM 25          22              7
        7                       BCM 4           7               8
        8                       BCM 2           3               9
        9                       BCM 3           5               10
        10                      BCM 8           24              11
        11                      BCM 7           26              12
        21                      BCM 5           29              13
        13                      BCM 9           21              14



        MATRIX numbering scheme for reference:
        
                1       2       3       4       5       6       7       8

        A       X       X       X       X       X       X       X       X
        B       X       X       X       X       X       X       X       X
        C       X       X       X       X       X       X       X       X
        D       X       X       X       X       X       X       X       X
        E       X       X       X       X       X       X       X       X
        F       X       X       X       X       X       X       X       X
        G       X       X       X       X       X       X       X       X
        H       X       X       X       X       X       X       X       X


        PIN CONTROL
        
        ROW1 [A]: PIN 9
        ROW2 [B]: PIN 14
        ROW3 [C]: PIN 8
        ROW4 [D]: PIN 12
        ROW5 [E]: PIN 1
        ROW6 [F]: PIN 7
        ROW7 [G]: PIN 2
        ROW8 [H]: PIN 5

"""

import sys
import wiringpi as wpi


# pin to wiringPi
ROW1 = 8
ROW2 = 13
ROW3 = 7
ROW4 = 11
ROW5 = 0
ROW6 = 6
ROW7 = 1
ROW8 = 4
COL1 = 21
COL2 = 2
COL3 = 3
COL4 = 9
COL5 = 5
COL6 = 10
COL7 = 14
COL8 = 15

HIGH = 1
LOW = 0



''' function to set all pins off in the matrix '''
def alloff():

        for pin in range(16):
                wpi.digitalWrite(pin, 0)  # turn all pins off

''' function to set all row control pins on in the matrix '''
def allrowson():

        wpi.digitalWrite(0,1)
        wpi.digitalWrite(1,1)
        wpi.digitalWrite(4,1)
        wpi.digitalWrite(6,1)
        wpi.digitalWrite(7,1)
        wpi.digitalWrite(8,1)
        wpi.digitalWrite(11,1)
        wpi.digitalWrite(13,1)


''' function to set all column control pins on in the matrix, turns off corresponding leds '''
def allcolson():

        wpi.digitalWrite(2,1)
        wpi.digitalWrite(3,1)
        wpi.digitalWrite(5,1)
        wpi.digitalWrite(9,1)
        wpi.digitalWrite(10,1)
        wpi.digitalWrite(21,1)
        wpi.digitalWrite(14,1)
        wpi.digitalWrite(15,1)

def main():

    ''' http://raspi.tv/2013/how-to-use-wiringpi2-for-python-on-the-raspberry-pi-in-raspbian '''

    wpi.wiringPiSetup()  # use wiringPi pin numbers
    #wpi.wiringPiSetupGpio()  # use gpio port numbers



    ## wpi.pinMode(pin_number, usage_code)
    ## usage_code: 0 for input, 1 for output, 2 for alt. function


    ## set all pins to output
    ## to reduce possibility of incorrect setup set each pin individually
    wpi.pinMode(0, 1)
    wpi.pinMode(1, 1)
    wpi.pinMode(2, 1)
    wpi.pinMode(3, 1)
    wpi.pinMode(4, 1)
    wpi.pinMode(5, 1)
    wpi.pinMode(6, 1)
    wpi.pinMode(7, 1)
    wpi.pinMode(8, 1)
    wpi.pinMode(9, 1)
    wpi.pinMode(10, 1)
    wpi.pinMode(11, 1)
    wpi.pinMode(21, 1)
    wpi.pinMode(13, 1)
    wpi.pinMode(14, 1)
    wpi.pinMode(15, 1)

    ## turn off all pins
    alloff()


    allrowson()
    #allcolson()


    # success

if __name__ == '__main__':
    status = main()
    sys.exit(status)
