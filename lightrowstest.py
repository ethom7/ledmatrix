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
rows = [8, 13, 7, 11, 0, 6, 1, 4]
columns = [21, 2, 3, 9, 5, 10, 14, 15]

high = 1
low = 0



''' function to set all pins off in the matrix '''
def alloff():
    for pin in range(16):
        wpi.digitalWrite(pin, 0)  # turn all pins off

''' function to set all row control pins on in the matrix '''
def allrowson():
    for row in rows:
        wpi.digitalWrite(row, 1)

''' function to set all column control pins on in the matrix, turns off corresponding leds '''
def allcolson():
    for column in columns:
        wpi.digitalWrite(column, 1)

def main():

    ''' http://raspi.tv/2013/how-to-use-wiringpi2-for-python-on-the-raspberry-pi-in-raspbian '''

    wpi.wiringPiSetup()  # use wiringPi pin numbers
    #wpi.wiringPiSetupGpio()  # use gpio port numbers



    ## wpi.pinMode(pin_number, usage_code)
    ## usage_code: 0 for input, 1 for output, 2 for alt. function


    ## set all pins to output
    ## to reduce possibility of incorrect setup set each pin individually
    for pin in (rows + columns):
        wpi.pinMode(pin, 1)

    ## turn off all pins
    alloff()


    allrowson()
    #allcolson()


    # success

if __name__ == '__main__':
    status = main()
    sys.exit(status)
