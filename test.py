"""
	lightrowstest.py

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
import time
import random
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


##---Letters------------------------------------------------------------------#

'''  
nested list containing the coordinates for each alphanum character.

#while (True):
		
	#	for coordinate in alphanumeric:
			row = 0
			column = 1
	#		paintcoordinates(coordinate[row], coordinate[column])

'''

thelist = [
			'A','B','C','D','E',
			'F','G','H','I','J',
			'K','L','M','N','O',
			'P','Q','R','S','T',
			'U','V','W','X','Y',
			'Z','0','1','2','3',
			'4','5','6','7','8',
			'9'
		]

alphanumdict = {      
				'A' : [[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 1], [4, 2], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 3]],
				'B' : [[0, 1], [0, 2], [0, 3], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 1], [3, 2], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 1], [7, 2]],
				'C' : [[0, 1], [0, 2], [0, 3], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 1], [7, 2], [7, 3]],
				'D' : [[0, 0], [0, 1], [0, 2], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 1], [7, 2]],
				'E' : [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [2, 0], [3, 0], [3, 1], [3, 2], [4, 0], [5, 0], [6, 0], [7, 0], [7, 1], [7, 2], [7, 3]],
				'F' : [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [2, 0], [3, 0], [3, 1], [3, 2], [4, 0], [5, 0], [6, 0], [7, 0]],
				'G' : [[0, 1], [0, 2], [0, 3], [1, 0], [2, 0], [3, 0], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 1], [7, 2], [7, 3]],
				'H' : [[0, 0], [0, 3], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 3]],
				'I' : [[0, 0], [0, 1], [0, 2], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 0], [7, 1], [7, 2]],
				'J' : [[0, 1], [0, 2], [0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 1], [6, 3], [7, 2]],
				'K' : [[0, 0], [0, 2], [1, 0], [1, 2], [2, 0], [2, 2], [3, 0], [3, 1], [4, 0], [4, 1], [4, 2], [5, 0], [5, 2], [6, 0], [6, 2], [7, 0], [7, 2]],
				'L' : [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [7, 1], [7, 2], [7, 3]],
				'M' : [[0, 0], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 3]],
				'N' : [[0, 0], [0, 1], [0, 2], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 3]],
				'O' : [[0, 1], [0, 2], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 1], [7, 2]],
				'P' : [[0, 0], [0, 1], [0, 2], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 1], [3, 2], [4, 0], [5, 0], [6, 0], [7, 0]],
				'Q' : [[0, 1], [1, 0], [1, 2], [2, 0], [2, 2], [3, 0], [3, 2], [4, 0], [4, 2], [5, 0], [5, 2], [6, 0], [6, 1], [7, 1], [7, 2]],
				'R' : [[0, 0], [0, 1], [0, 2], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 1], [3, 2], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 3]],
				'S' : [[0, 1], [0, 2], [0, 3], [1, 0], [2, 0], [3, 1], [3, 2], [3, 3], [4, 3], [5, 3], [6, 3], [7, 0], [7, 1], [7, 2]],
				'T' : [[0, 0], [0, 1], [0, 2], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]],
				'U' : [[0, 0], [0, 3], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 1], [7, 2], [7, 3]],
				'V' : [[0, 0], [0, 3], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 1], [6, 2], [7, 1], [7, 2]],
				'W' : [[0, 0], [0, 3], [1, 0], [1, 3], [2, 0], [2, 3], [3, 3], [3, 0], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 1], [6, 2], [6, 3], [7, 0], [7, 3]],
				'X' : [[0, 0], [0, 3], [1, 0], [1, 3], [2, 0], [2, 3], [3, 1], [3, 2], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 3]],
				'Y' : [[0, 0], [0, 2], [1, 0], [1, 2], [2, 0], [2, 2], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]],
				'Z' : [[0, 0], [0, 1], [0, 2], [0, 3], [1, 3], [2, 2], [3, 1], [3, 2], [4, 1], [4, 2], [5, 1], [6, 0], [7, 0], [7, 1], [7, 2], [7, 3]],
				'0' : [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 1], [7, 2], [7, 3]],
				'1' : [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3]],
				'2' : [[0, 0], [0, 1], [0, 2], [0, 3], [1, 3], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [4, 0], [5, 0], [6, 0], [7, 0], [7, 1], [7, 2], [7, 3]],
				'3' : [[0, 0], [0, 1], [0, 2], [0, 3], [1, 3], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [4, 3], [5, 3], [6, 3], [7, 0], [7, 1], [7, 2], [7, 3]],
				'4' : [[0, 0], [0, 3], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3]],
				'5' : [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [2, 0], [3, 0], [3, 1], [3, 2], [3, 3], [4, 3], [5, 3], [6, 3], [7, 0], [7, 1], [7, 2], [7, 3]],
				'6' : [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [2, 0], [3, 0], [3, 1], [3, 2], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 1], [7, 2], [7, 3]],
				'7' : [[0, 0], [0, 1], [0, 2], [0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3]],
				'8' : [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 1], [7, 2], [7, 3]],
				'9' : [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3]]
				}



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

''' function to set all row control pins on in the matrix '''
def allrowson():

	for pin in rows:
		wpi.digitalWrite(pin, HIGH)
	
''' 
	Function that will begin at A1 and move to A8 down to B1 over 
	to repeat through the remainder of the matrix. Ends on H8.  
'''

def walkthematrix():

	## traverse rows
	for row in rows:
		iteration = 0
		print "Row " + str(row)
		wpi.digitalWrite(row, HIGH)  #turn on the row

		for col in cols:
			wpi.digitalWrite(col, HIGH)
		
		for col in cols:
			if col == cols[iteration]:
				wpi.digitalWrite(col, LOW)  #turn on col to light led

				## sleep delay timing: 
				## solid = .00005, row solid = .005, 
				## 4 lighted = .015, 2 lighted = .02, 
				## single = .05
				time.sleep(.0005)  #number of display seconds

				#led off
				wpi.digitalWrite(cols[iteration], HIGH)

			iteration += 1

		wpi.digitalWrite(row, LOW)

		
''' 
	Function that will begin at A1 and move to A8 down to B1 over 
	to repeat through the remainder of the matrix. Ends on H8.  
'''

def walkthematrixcols():

	## traverse rows
	for col in cols:
		iteration = 0
		print "Col " + str(col)
		wpi.digitalWrite(col, HIGH)  #turn on the row

		for row in rows:
			wpi.digitalWrite(row, HIGH)
		
		for row in rows:
			if row == rows[iteration]:
				wpi.digitalWrite(row, LOW)  #turn on col to light led

				## sleep delay timing: 
				## solid = .00005, row solid = .005, 
				## 4 lighted = .015, 2 lighted = .02, 
				## single = .05
				time.sleep(.02)  #number of display seconds

				#led off
				wpi.digitalWrite(rows[iteration], HIGH)

			iteration += 1

		wpi.digitalWrite(col, LOW)
		



def paintcoordinates(rownum, colnum):

	alloff()

	#print "Row : " + str(rownum) + " Col : " + str(colnum)

	wpi.digitalWrite(rows[rownum], HIGH)  #turn on the row

	for col in cols:
		wpi.digitalWrite(col, HIGH)
		
	wpi.digitalWrite(cols[colnum], LOW)  #turn on col to light led

	## sleep delay timing: 
	## solid = .00005, row solid = .005, 
	## 4 lighted = .015, 2 lighted = .02, 
	## single = .05
	time.sleep(.0005)  #number of display seconds

	
def randomint():

	return random.randint(0,7)
		

def scroll(alphanumeric):

	matrixwidth = 8
	#matrixheight = 8



	



##---Main---------------------------------------------------------------------#

def main():
	
	setup()

	#allrowson()
	#while (True):

	for letter in thelist:
		offset = 7
		for count in range(1000):
			if count % 20 == 0:
				offset -= 1
			for coord in alphanumdict[letter]:
				if offset >= -3:
					if coord[1]+offset >=0 and coord[1]+offset <= 7:
						paintcoordinates(coord[0], coord[1]+offset)
				else:
					offset = 7

	


	alloff()

	# success

if __name__ == '__main__':
	status = main()
	sys.exit(status)
