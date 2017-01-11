"""
	font.py

	Program is to provide support for the ledmatrix.
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

blankmatrix = [
			    [' ',' ',' ',' ',' ',' ',' ',' '],
			    [' ',' ',' ',' ',' ',' ',' ',' '],
			    [' ',' ',' ',' ',' ',' ',' ',' '],
			    [' ',' ',' ',' ',' ',' ',' ',' '],
			    [' ',' ',' ',' ',' ',' ',' ',' '],
			    [' ',' ',' ',' ',' ',' ',' ',' '],
			    [' ',' ',' ',' ',' ',' ',' ',' '],
			    [' ',' ',' ',' ',' ',' ',' ',' ']
			  ]

'''  
nested list containing the coordinates for each alphanum character.

#while (True):
		
	#	for coordinate in alphanumeric:
			row = 0
			column = 1
	#		paintcoordinates(coordinate[row], coordinate[column])

'''
alphanumA = [[0,3],[0,4],[1,2],[1,3],[1,4],[1,5],[2,2],[2,5],[3,2],[3,5],[4,2],[4,3],[4,4],[4,5],[5,2],[5,5],[6,2],[6,5],[7,2],[7,5]]
alphanumB = [[0,3],[0,4],[0,5],[1,2],[1,5],[2,2],[2,5],[3,2],[3,3],[3,4],[4,2],[4,5],[5,2],[6,2],[6,5],[7,2],[7,3],[7,4]]
alphanumC = [[0,3],[0,4],[0,5],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,3],[7,4],[7,5]]
alphanumD = [[0,2],[0,3],[0,4],[1,2],[1,5],[2,2],[2,5],[3,2],[3,5],[4,2],[4,5,],[5,2],[5,5],[6,2],[6,5],[7,2],[7,3],[7,4]]
alphanumE = [[0,2],[0,3],[0,4],[0,5],[1,2],[2,2],[3,2],[3,3],[3,4],[4,2],[5,2],[6,2],[7,2],[7,3],[7,4],[7,5]]
alphanumF = [[0,2],[0,3],[0,4],[0,5],[1,2],[2,2],[3,2],[3,3],[3,4],[4,2],[5,2],[6,2],[7,2]]
alphanumG = [[0,3],[0,4],[0,5],[1,2],[2,2],[3,2],[4,2],[4,5],[5,2],[5,5],[6,2],[6,5],[7,3],[7,4],[7,5]]
alphanumH = [[0,2],[0,5],[1,2],[1,5],[2,2],[2,5],[3,2],[3,3],[3,4],[3,5],[4,2],[4,5],[5,2],[5,5],[6,2],[6,5],[7,2],[7,5]]
alphanumI = [[0,2],[0,3],[0,4],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,2],[7,3],[7,4]]
alphanumJ = [[0,3],[0,4],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,3],[6,5],[7,4]]
alphanumK = [[0,2],[0,4],[1,2],[1,4],[2,2],[2,4],[3,2],[3,3],[4,2],[4,3],[4,4],[5,2],[5,4],[6,2],[6,4],[7,2],[7,4]]
alphanumL = [[0,2],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[7,3],[7,4],[7,5]]
alphanumM = [[0,2],[0,5],[1,2],[1,3],[1,4],[1,5],[2,2],[2,5],[3,2],[3,5],[4,2],[4,5],[5,2],[5,5],[6,2],[6,5],[7,2],[7,5]]
alphanumN = [[0,2],[0,3],[0,4],[1,2],[1,5],[2,2],[2,5],[3,2],[3,5],[4,2],[4,5,],[5,2],[5,5],[6,2],[6,5],[7,2],[7,5]]
alphanumO = [[0,3],[0,4],[1,2],[1,5],[2,2],[2,5],[3,2],[3,5],[4,2],[4,5],[5,2],[5,5],[6,2],[6,5],[7,3],[7,4]]
alphanumP = [[0,2],[0,3],[0,4],[1,2],[1,5],[2,2],[2,5],[3,2],[3,3],[3,4],[4,2],[5,2],[6,2],[7,2]]
alphanumQ = [[0,3],[1,2],[1,4],[2,2],[2,4],[3,2],[3,4],[4,2],[4,4],[5,2],[5,4],[6,2],[6,3],[7,3],[7,4]]
alphanumR = [[0,2],[0,3],[0,4],[1,2],[1,5],[2,2],[2,5],[3,2],[3,3],[3,4],[4,2],[4,5],[5,2],[5,5],[6,2],[6,5],[7,2],[7,5]]
alphanumS = [[0,3],[0,4],[0,5],[1,2],[2,2],[3,3],[3,4],[3,5],[4,5],[5,5],[6,5],[7,2],[7,3],[7,4]]
alphanumT = [[0,2],[0,3],[0,4],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3]]
alphanumU = [[0,2],[0,5],[1,2],[1,5],[2,2],[2,5],[3,2],[3,5],[4,2],[4,5],[5,2],[5,5],[6,2],[6,5],[7,3],[7,4],[7,5]]
alphanumV = [[0,2],[0,5],[1,2],[1,5],[2,2],[2,5],[3,2],[3,5],[4,2],[4,5],[5,2],[5,5],[6,3],[6,4],[7,3],[7,4]]
alphanumW = [[0,2],[0,5],[1,2],[1,5],[2,2],[2,5],[3,5],[3,2],[3,5],[4,2],[4,5],[5,2],[5,5],[6,2],[6,3],[6,4],[6,5],[7,2],[7,5]]
alphanumX = [[0,2],[0,5],[1,2],[1,5],[2,2],[2,5],[3,3],[3,4],[4,2],[4,5],[5,2],[5,5],[6,2],[6,5],[7,2],[7,5]]
alphanumY = [[0,2],[0,4],[1,2],[1,4],[2,2],[2,4],[3,3],[4,3],[5,3],[6,3],[7,3]]
alphanumZ = [[0,2],[0,3],[0,4],[0,5],[1,5],[2,4],[3,3],[3,4],[4,3],[4,4],[5,3],[6,2],[7,2],[7,3],[7,4],[7,5]]
alphanum0 = [[0,2],[0,3],[0,4],[0,5],[1,2],[1,5],[2,2],[2,5],[3,2],[3,5],[4,2],[4,5],[5,2],[5,5],[6,2],[6,5],[7,2],[7,3],[7,4],[7,5]]
alphanum1 = [[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5]]
alphanum2 = [[0,2],[0,3],[0,4],[0,5],[1,5],[2,5],[3,2],[3,3],[3,4],[3,5],[4,2],[5,2],[6,2],[7,2],[7,3],[7,4],[7,5]]
alphanum3 = [[0,2],[0,3],[0,4],[0,5],[1,5],[2,5],[3,2],[3,3],[3,4],[3,5],[4,5],[5,5],[6,5],[7,2],[7,3],[7,4],[7,5]]
alphanum4 = [[0,2],[0,5],[1,2],[1,5],[2,2],[2,5],[3,2],[3,3],[3,4],[3,5],[4,5],[5,5],[6,5],[7,5]]
alphanum5 = [[0,2],[0,3],[0,4],[0,5],[1,2],[2,2],[3,2],[3,3],[3,4],[3,5],[4,5],[5,5],[6,5],[7,2],[7,3],[7,4],[7,5]]
alphanum6 = [[0,2],[0,3],[0,4],[0,5],[1,2],[2,2],[3,2],[3,3],[3,4],[3,5],[4,2],[4,5],[5,2],[5,5],[6,2],[6,5],[7,2],[7,3],[7,4],[7,5]]
alphanum7 = [[0,2],[0,3],[0,4],[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5]]
alphanum8 = [[0,2],[0,3],[0,4],[0,5],[1,2],[1,5],[2,2],[2,5],[3,2],[3,3],[3,4],[3,5],[4,2],[4,5],[5,2],[5,5],[6,2],[6,5],[7,2],[7,3],[7,4],[7,5]]
alphanum9 = [[0,2],[0,3],[0,4],[0,5],[1,2],[1,5],[2,2],[2,5],[3,2],[3,3],[3,4],[3,5],[4,5],[5,5],[6,5],[7,5]]

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

	wpi.digitalWrite(rownum, HIGH)  #turn on the row

	for col in cols:
		wpi.digitalWrite(col, HIGH)
		
	wpi.digitalWrite(colnum, LOW)  #turn on col to light led

	## sleep delay timing: 
	## solid = .00005, row solid = .005, 
	## 4 lighted = .015, 2 lighted = .02, 
	## single = .05
	time.sleep(.005)  #number of display seconds


## function generate a pseudo-random integer between 0 and 7 for random led lighting
def randomint():

	return random.randint(0,7)
	

## function to analog print the matrix for the letter
def printmatrix(alphanumeric):

	outmatrix = blankmatrix

	for pair in alphanumeric:

			outmatrix[pair[0]][pair[1]] = 'O'

	return outmatrix



##---Main---------------------------------------------------------------------#

def main():
	
	#setup()

	
	#readcharacter(anA)

	out4 = printmatrix(alphanum9)

	for i in out4:
		print i

	#while (True):
		
	#	for entry in alphanum9:
	#		paintcoordinates(entry[0], entry[1])
		#walkthematrix()
		#walkthematrixcols()

	# success

if __name__ == '__main__':
	status = main()
	sys.exit(status)
