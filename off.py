"""
	matrixoff.py

	Script is to drive the 16 pin 8x8 led matrix using WiringPi and Python.
	by Evan Thompson
	January 3, 2017
	https://github.com/ethom7/ledmatrix


	WiringPi		Rpi 		PIN		LED PIN
	0			BCM 17		11		1
	1			BCM 18		12		2
	2			BCM 27		13		3
	3			BCM 22		15		4
	4			BCM 23		16		5
	5			BCM 24		18		6
	6			BCM 25		22		7
	7			BCM 4		7		8
	8			BCM 2		3		9
	9			BCM 3		5		10
	10			BCM 8		24		11
	11			BCM 7		26		12
	21			BCM 5		29		13
	13			BCM 9		21		14



	MATRIX 
		1	2	3	4	5	6	7	8

	A	X	X	X	X	X	X	X	X
	B	X	X	X	X	X	X	X	X
	C	X	X	X	X	X	X	X	X
	D	X	X	X	X	X	X	X	X
	E	X	X	X	X	X	X	X	X
	F	X	X	X	X	X	X	X	X
	G	X	X	X	X	X	X	X	X
	H	X	X	X	X	X	X	X	X
	

"""
##---Imports------------------------------------------------------------------#
import sys
import wiringpi as wpi 


##---Variables----------------------------------------------------------------#

# pin to wiringPi for rows and columns 
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

#list containing the pin reference for the row pins
rows = [ROW1, ROW2, ROW3, ROW4, ROW5, ROW6, ROW7, ROW8]

#list containing the pin reference for the column pins
cols = [COL1, COL2, COL3, COL4, COL5, COL6, COL7, COL8]

## to reduce possibility of incorrect setup set each pin individually
wpipinslist = [
				0, 1, 2, 3, 4, 
				5, 6, 7, 8, 9, 
				10, 11, 21, 13, 
				14, 15
				]


##---Functions----------------------------------------------------------------#

''' setup function '''
def setup():

	''' http://raspi.tv/2013/how-to-use-wiringpi2-for-python-on-the-raspberry-pi-in-raspbian '''
	
	wpi.wiringPiSetup()  # use wiringPi pin numbers
	#wpi.wiringPiSetupGpio()  # use gpio port numbers

	## wpi.pinMode(pin_number, usage_code)
	## usage_code: 0 for input, 1 for output, 2 for alt. function
	useage = 1

	
	##wpipinslist is defined and set in variables
	
	## set all pins
	for pin in wpipinslist:
		wpi.pinMode(pin, useage)


	## turn off all pins
	alloff()

	
##---Helper Functions---------------------------------------------------------#


''' function to set all pins off in the matrix '''
def alloff():

	for pin in wpipinslist:
		wpi.digitalWrite(pin, LOW)  # turn all pins off




##---Main---------------------------------------------------------------------#

def main():
	
	setup()



	# success

if __name__ == '__main__':
	status = main()
	sys.exit(status)
