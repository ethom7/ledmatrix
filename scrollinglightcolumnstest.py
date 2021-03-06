"""
	scrollinglightcolumnstest.py

	Script is to drive the 16 pin 8x8 led matrix using WiringPi and Python which will serve as the 
	software driven led matrix display solution. The function convertstringfordisplay(text) converts a string 
	of ASCII characters [A-Z], [0-9], and [,.:!] to a list containing column row coordinates. The function 
	counterfunction(outpanel) is a loop to scroll the displaypanellist returned from convertstringfordisplay(text).
	The current program needs cleaning and the display needs additional work but does provide some of the 
	desired functionality.
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
		0 	1	2	3	4	5	6	7

	0	X	X	X	X	X	X	X	X
	1	X	X	X	X	X	X	X	X
	2	X	X	X	X	X	X	X	X
	3	X	X	X	X	X	X	X	X
	4	X	X	X	X	X	X	X	X
	5	X	X	X	X	X	X	X	X
	6	X	X	X	X	X	X	X	X
	7	X	X	X	X	X	X	X	X
	

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
cols = [COL1, COL2, COL3, COL4, COL5, COL6, COL7, COL8]  # regular indexed

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
			'9',',',':','!','.'
		]

alphanumwidth = {      
				'A' : 4, 'B' : 4, 'C' : 4, 'D' : 4,
				'E' : 4, 'F' : 4, 'G' : 4, 'H' : 4,
				'I' : 3, 'J' : 3, 'K' : 3, 'L' : 4,
				'M' : 4, 'N' : 4, 'O' : 4, 'P' : 4,
				'Q' : 3, 'R' : 4, 'S' : 4, 'T' : 3,
				'U' : 4, 'V' : 4, 'W' : 4, 'X' : 4,
				'Y' : 3, 'Z' : 4, '0' : 4, '1' : 1,
				'2' : 4, '3' : 4, '4' : 4, '5' : 4,
				'6' : 4, '7' : 4, '8' : 4, '9' : 4,
				',' : 2, ':' : 1, '!' : 1, '.' : 1,
				'sp' : 2
				}

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
				'9' : [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3]],
				',' : [[5,1],[6,1],[7,0]],
				':' : [[3,0],[5,0]],
				'!' : [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[7,0]],
				'.' : [[7,0]]
				}

displaypanellist = [[],[],[],[],[],[],[],[]]  # each entry in list is the full row for the display



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
	alllow()
	#allhigh()

	
##---Helper Functions---------------------------------------------------------#


''' function to set all pins to LOW in the matrix '''
def alllow():

	for pin in wpipinslist:
		wpi.digitalWrite(pin, LOW)  # turn all pins off


""" 
	function will set all pins to high. This will leave all the leds off. 
""" 
def allhigh():

	for pin in wpipinslist:
		wpi.digitalWrite(pin, HIGH)  # set all pins to HIGH

''' function to set all row control pins on in the matrix '''
def allrowson():

	for pin in rows:
		wpi.digitalWrite(pin, HIGH)



''' function to set all row control pins on in the matrix '''
def allrowsoff():

	for pin in rows:
		wpi.digitalWrite(pin, LOW)
	


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

	alllow()

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
		


	
""" 
	function tests column based led lighting. By setting a specified column 
	to LOW, all rows that are HIGH will be lighted. 
"""
def testcols(column):
	
	## set rows and columns HIGH, 
	## turn off row setting LOW and turn on column setting HIGH.
	allhigh()  


	wpi.digitalWrite(cols[int(column)], LOW)





""" 
	function implements column based led lighting. By setting a specified column 
	to LOW, all rows that are HIGH will be lighted. 
"""
def display(outputpanel):
	
	## set rows and columns HIGH, 
	## turn off row setting LOW and turn on column setting HIGH.
	allhigh()

	#for columns in range(len(outputpanel)):
	counter = 0
	total = 100
	

	## number of times to scroll entire text
	while counter < total:

		
		## number of times to display the column matrix loop
		for outer in range(len(outputpanel)):

			if outer+counter < len(outputpanel):

				for row in outputpanel[outer+counter]:
					
					wpi.digitalWrite(cols[int((outer+counter) % 8)], LOW)  # turn on column

					for rowindex in range(len(outputpanel[outer+counter])):

						wpi.digitalWrite(rows[outputpanel[int(outer+counter)][int(rowindex)]], HIGH)  # turn on row


					time.sleep(.0005)

					wpi.digitalWrite(cols[int((outer+counter) % 8)], HIGH)  # turn off column

					for x in range(8):
						wpi.digitalWrite(rows[x], LOW)


		counter += 1
	

	"""
	while counter < len(outputpanel):

		for number in range(1000):  # number of repetions
			tempcount = counter

			for columns in range(8):  # number of display columns
				tempcount += columns

				
				if outputpanel[tempcount] != []:
			 
					wpi.digitalWrite(cols[int(tempcount % 8)], LOW)  # turn on column

					for rowindex in range(len(outputpanel[tempcount])):

						wpi.digitalWrite(rows[outputpanel[int(tempcount)][int(rowindex)]], HIGH)  # turn on row


					time.sleep(.0005)

					wpi.digitalWrite(cols[int(tempcount % 8)], HIGH)  # turn off column

					for x in range(8):
						wpi.digitalWrite(rows[x], LOW)

			
		counter += 1
		"""	








'''
	Function is a demo showing scrolling display of the alphanumeric
	characters.
'''

def scrollalphanumtest():

	setup()

	for letter in alphanumlist:  # loop thru each entry in the alphanum list
		offset = 7  # total columns minus 1. 8-1=7
		for count in range(1000):  # number of loops thru each character, controls how long each character is displayed
			if count % 20 == 0:  # every 20 times thru each character subtract 1 from the display column, controls the scrolling speed
				offset -= 1
			for coord in alphanumdict[
				letter]:  # loop thru each display point in the alphanumdict[letter] character list
				if offset >= -3:  # if offset is beyond the display boundary of the last column, max char width is 4
					if coord[1] + offset >= 0 and coord[
						1] + offset <= 7:  # if the coordinate is within the viewable area paint the coordinate to the display
						paintcoordinates(coord[0], coord[1] + offset)
				else:
					offset = 7  # reset the offset to initial setting

	alllow()	


def testconsoledemo():

	print "Running Setup..."

	setup()

	alllow()
	

	orientation = raw_input("row or column? ")
	number = raw_input("applicable row/column index: ")
	selection = raw_input("high or low?")

	if orientation.lower() == 'row':
		if selection.lower() == "high":
			wpi.digitalWrite(rows[int(number)], HIGH)
		else:
			wpi.digitalWrite(rows[int(number)], LOW)
	else:
		if selection.lower() == "high":
			wpi.digitalWrite(cols[int(number)], HIGH)
		else:
			for row in rows:
				wpi.digitalWrite(row, HIGH)
			wpi.digitalWrite(cols[int(number)], LOW)
			for col in cols:
				if col != cols[int(number)]:
					wpi.digitalWrite(col, HIGH)



"""
	Function takes a string of alphanumeric characters [A-Z], [0-9], [,.!:], 
	and spaces. Returns nested list named outputpanel, structured as followed:
		outputpanel[character] = a list containing a list of columns for each character
		outputpanel[character][column] = a list of int's for the row



"""

def convertstringfordisplay(text):

	displaypanel = []  # main list containing all columns for each letter

	text = text.upper()

	characterlist = []  # list containing each character from the string
	for character in text:
		if character != ' ':
			coordinateslist = alphanumdict[character]
			characterlist.append(coordinateslist)
		else:
			characterlist.append([])

	#print characterlist  #output when letters are entry to list: ['H', 'I', ',', ' ', 'M', 'Y', ' ', 'N', 'A', 'M', 'E', ' ', 'I', 'S', ' ', 'E', 'V', 'A', 'N', '!']

	""" coordinates to list, 
		characterlist[character] is coordinates for that letter
		[[0, 0], [0, 3], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 3]]
		[[0, 0], [0, 1], [0, 2], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 0], [7, 1], [7, 2]]
		[[5, 1], [6, 1], [7, 0]]
		[]
		[[0, 0], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 3]]
		[[0, 0], [0, 2], [1, 0], [1, 2], [2, 0], [2, 2], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]]
		[]
		[[0, 0], [0, 1], [0, 2], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 3]]
		[[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 1], [4, 2], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 3]]
		[[0, 0], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 3]]
		[[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [2, 0], [3, 0], [3, 1], [3, 2], [4, 0], [5, 0], [6, 0], [7, 0], [7, 1], [7, 2], [7, 3]]
		[]
		[[0, 0], [0, 1], [0, 2], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 0], [7, 1], [7, 2]]
		[[0, 1], [0, 2], [0, 3], [1, 0], [2, 0], [3, 1], [3, 2], [3, 3], [4, 3], [5, 3], [6, 3], [7, 0], [7, 1], [7, 2]]
		[]
		[[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [2, 0], [3, 0], [3, 1], [3, 2], [4, 0], [5, 0], [6, 0], [7, 0], [7, 1], [7, 2], [7, 3]]
		[[0, 0], [0, 3], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 1], [6, 2], [7, 1], [7, 2]]
		[[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 1], [4, 2], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 3]]
		[[0, 0], [0, 1], [0, 2], [1, 0], [1, 3], [2, 0], [2, 3], [3, 0], [3, 3], [4, 0], [4, 3], [5, 0], [5, 3], [6, 0], [6, 3], [7, 0], [7, 3]]
		[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [7, 0]]

	"""

	

	for ch in characterlist:  # for each character in the characterlist
		charactercolumns = [[],[],[],[],[],[],[],[]]
		for row,column in ch:
			charactercolumns[column].append(row)

		displaypanel.append(charactercolumns)

	#print displaypanel
		

	#count = 0
	#for ch in displaypanel:
	#	print "letter: " + text[count] + " " + str(ch)
	#	count +=1
	

	## accomplishes the following:

	"""
		displaypanel[letter][columnindex] = row
		letter: H [[0, 1, 2, 3, 4, 5, 6, 7], [3], [3], [0, 1, 2, 3, 4, 5, 6, 7], [], [], [], []]  			# 6
		letter: I [[0, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 7], [], [], [], [], []]							# 5
		letter: , [[7], [5, 6], [], [], [], [], [], []]														# 4
		letter:   [[], [], [], [], [], [], [], []]															# 2
		letter: M [[0, 1, 2, 3, 4, 5, 6, 7], [1], [1], [0, 1, 2, 3, 4, 5, 6, 7], [], [], [], []]			# 6
		letter: Y [[0, 1, 2], [3, 4, 5, 6, 7], [0, 1, 2], [], [], [], [], []]								# 5
		letter:   [[], [], [], [], [], [], [], []]															# 2
		letter: N [[0, 1, 2, 3, 4, 5, 6, 7], [0], [0], [1, 2, 3, 4, 5, 6, 7], [], [], [], []]				# 6
		letter: A [[1, 2, 3, 4, 5, 6, 7], [0, 1, 4], [0, 1, 4], [1, 2, 3, 4, 5, 6, 7], [], [], [], []]		# 6
		letter: M [[0, 1, 2, 3, 4, 5, 6, 7], [1], [1], [0, 1, 2, 3, 4, 5, 6, 7], [], [], [], []]			# 6
		letter: E [[0, 1, 2, 3, 4, 5, 6, 7], [0, 3, 7], [0, 3, 7], [0, 7], [], [], [], []]					# 6
		letter:   [[], [], [], [], [], [], [], []]															# 2
		letter: I [[0, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 7], [], [], [], [], []]							# 5
		letter: S [[1, 2, 7], [0, 3, 7], [0, 3, 7], [0, 3, 4, 5, 6], [], [], [], []]						# 6
		letter:   [[], [], [], [], [], [], [], []]															# 2
		letter: E [[0, 1, 2, 3, 4, 5, 6, 7], [0, 3, 7], [0, 3, 7], [0, 7], [], [], [], []]					# 6
		letter: V [[0, 1, 2, 3, 4, 5], [6, 7], [6, 7], [0, 1, 2, 3, 4, 5], [], [], [], []]					# 6
		letter: A [[1, 2, 3, 4, 5, 6, 7], [0, 1, 4], [0, 1, 4], [1, 2, 3, 4, 5, 6, 7], [], [], [], []]		# 6
		letter: N [[0, 1, 2, 3, 4, 5, 6, 7], [0], [0], [1, 2, 3, 4, 5, 6, 7], [], [], [], []]				# 6
		letter: ! [[0, 1, 2, 3, 4, 5, 7], [], [], [], [], [], [], []]										# 3


		len(finallist) = 96  #columns in finallist
		




		'''  outputpanel structure  '''

		#final should contain the following data
		finallist = [
					  [0, 1, 2, 3, 4, 5, 6, 7],  #H
					  [3], 
					  [3], 
					  [0, 1, 2, 3, 4, 5, 6, 7], 
					  [], 
					  [],
					  [0, 7],                    #I
					  [0, 1, 2, 3, 4, 5, 6, 7], 
					  [0, 7], 
					  [], 
					  [],
					  [7],                       #,
					  [5, 6], 
					  [], 
					  [],
					  [],                        #SP
					  [], 
					  [0, 1, 2, 3, 4, 5, 6, 7],  #M
					  [1], 
					  [1], 
					  [0, 1, 2, 3, 4, 5, 6, 7], 
					  [], 
					  [],
					  [0, 1, 2],                 #Y
					  [3, 4, 5, 6, 7], 
					  [0, 1, 2], 
					  [], 
					  [],
					  [],                        #SP
					  [],
					  [0, 1, 2, 3, 4, 5, 6, 7],  #N
					  [0], 
					  [0], 
					  [1, 2, 3, 4, 5, 6, 7], 
					  [], 
					  [],
					  [1, 2, 3, 4, 5, 6, 7],     #A
					  [0, 1, 4], 
					  [0, 1, 4], 
					  [1, 2, 3, 4, 5, 6, 7], 
					  [], 
					  [],
					  [0, 1, 2, 3, 4, 5, 6, 7],  #M
					  [1], 
					  [1], 
					  [0, 1, 2, 3, 4, 5, 6, 7], 
					  [], 
					  [],
					  [0, 1, 2, 3, 4, 5, 6, 7],  #E
					  [0, 3, 7], 
					  [0, 3, 7], 
					  [0, 7], 
					  [], 
					  [],
					  [],                        #SP
					  [],
					  [0, 7],                    #I
					  [0, 1, 2, 3, 4, 5, 6, 7], 
					  [0, 7], 
					  [], 
					  [],
					  [1, 2, 7],                 #S
					  [0, 3, 7], 
					  [0, 3, 7], 
					  [0, 3, 4, 5, 6], 
					  [], 
					  [],
					  [],                        #SP
					  [],
					  [0, 1, 2, 3, 4, 5, 6, 7],  #E
					  [0, 3, 7], 
					  [0, 3, 7], 
					  [0, 7], 
					  [], 
					  [],
					  [0, 1, 2, 3, 4, 5],        #V
					  [6, 7], 
					  [6, 7], 
					  [0, 1, 2, 3, 4, 5], 
					  [], 
					  [],
					  [1, 2, 3, 4, 5, 6, 7],    #A 
					  [0, 1, 4], 
					  [0, 1, 4], 
					  [1, 2, 3, 4, 5, 6, 7], 
					  [], 
					  [],
					  [0, 1, 2, 3, 4, 5, 7],    #!
					  [], 
					  []
					]

	"""

	outputpanel = []
	for letter in range(len(displaypanel)):  # iterate thru each letter
		
		#check for a space and enter 
		if displaypanel[letter] == [[],[],[],[],[],[],[],[]]:
			outputpanel.append([])
			outputpanel.append([])
		  	# move to next letter
		else:
			#trim extra blank columns
			blankcount = 0
			for eachcol in range(len(displaypanel[letter])):
				popcol = displaypanel[letter][eachcol]
				
				if blankcount < 2:
					outputpanel.append(popcol)
					if popcol == []:
						blankcount +=1
				else:
					break


	""" raw print of the outputpanel 
	[[[0, 1, 2, 3, 4, 5, 6, 7], [3], [3], [0, 1, 2, 3, 4, 5, 6, 7], [], [], [], []], [[0, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 7], [], [], [], [], []], [[7], [5, 6], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[0, 1, 2, 3, 4, 5, 6, 7], [1], [1], [0, 1, 2, 3, 4, 5, 6, 7], [], [], [], []], [[0, 1, 2], [3, 4, 5, 6, 7], [0, 1, 2], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[0, 1, 2, 3, 4, 5, 6, 7], [0], [0], [1, 2, 3, 4, 5, 6, 7], [], [], [], []], [[1, 2, 3, 4, 5, 6, 7], [0, 1, 4], [0, 1, 4], [1, 2, 3, 4, 5, 6, 7], [], [], [], []], [[0, 1, 2, 3, 4, 5, 6, 7], [1], [1], [0, 1, 2, 3, 4, 5, 6, 7], [], [], [], []], [[0, 1, 2, 3, 4, 5, 6, 7], [0, 3, 7], [0, 3, 7], [0, 7], [], [], [], []], [[], [], [], [], [], [], [], []], [[0, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 7], [], [], [], [], []], [[1, 2, 7], [0, 3, 7], [0, 3, 7], [0, 3, 4, 5, 6], [], [], [], []], [[], [], [], [], [], [], [], []], [[0, 1, 2, 3, 4, 5, 6, 7], [0, 3, 7], [0, 3, 7], [0, 7], [], [], [], []], [[0, 1, 2, 3, 4, 5], [6, 7], [6, 7], [0, 1, 2, 3, 4, 5], [], [], [], []], [[1, 2, 3, 4, 5, 6, 7], [0, 1, 4], [0, 1, 4], [1, 2, 3, 4, 5, 6, 7], [], [], [], []], [[0, 1, 2, 3, 4, 5, 6, 7], [0], [0], [1, 2, 3, 4, 5, 6, 7], [], [], [], []], [[0, 1, 2, 3, 4, 5, 7], [], [], [], [], [], [], []]]
[[0, 1, 2, 3, 4, 5, 6, 7], [3], [3], [0, 1, 2, 3, 4, 5, 6, 7], [], [], [0, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 7], [], [], [7], [5, 6], [], [], [], [], [0, 1, 2, 3, 4, 5, 6, 7], [1], [1], [0, 1, 2, 3, 4, 5, 6, 7], [], [], [0, 1, 2], [3, 4, 5, 6, 7], [0, 1, 2], [], [], [], [], [0, 1, 2, 3, 4, 5, 6, 7], [0], [0], [1, 2, 3, 4, 5, 6, 7], [], [], [1, 2, 3, 4, 5, 6, 7], [0, 1, 4], [0, 1, 4], [1, 2, 3, 4, 5, 6, 7], [], [], [0, 1, 2, 3, 4, 5, 6, 7], [1], [1], [0, 1, 2, 3, 4, 5, 6, 7], [], [], [0, 1, 2, 3, 4, 5, 6, 7], [0, 3, 7], [0, 3, 7], [0, 7], [], [], [], [], [0, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 7], [], [], [1, 2, 7], [0, 3, 7], [0, 3, 7], [0, 3, 4, 5, 6], [], [], [], [], [0, 1, 2, 3, 4, 5, 6, 7], [0, 3, 7], [0, 3, 7], [0, 7], [], [], [0, 1, 2, 3, 4, 5], [6, 7], [6, 7], [0, 1, 2, 3, 4, 5], [], [], [1, 2, 3, 4, 5, 6, 7], [0, 1, 4], [0, 1, 4], [1, 2, 3, 4, 5, 6, 7], [], [], [0, 1, 2, 3, 4, 5, 6, 7], [0], [0], [1, 2, 3, 4, 5, 6, 7], [], [], [0, 1, 2, 3, 4, 5, 7], [], []]
	"""


	return outputpanel





def counterfunction(outputpanellist):

	allhigh()

	## scroll speed is controlled by columndisplayiterations and columndisplaylength

	scrolliterations = 10  # how many times to scroll thru the entire message
	columndisplayiterations = 25  # how many times each of the columns is lighted
	columndisplaylength = .0005  # how long each column is left lighted
	displaypanelwidth = 8  # how many columns are in the led matrix
	total = len(outputpanellist)  # the length of the panel list

	## times to fully scroll 
	## uncomment below to scroll thru entire message until interrupted
	# while True:
	for number in range(scrolliterations):
		counter = 0

		## iterate thru the full panellist
		while counter < total:

			#print "list index counter: " + str(counter)

			## number of repeating iterations thru the display panel
			for repeatdisplay in range(columndisplayiterations):

				## range of numbers in the list to count ahead, look ahead
				for lookahead in range(displaypanelwidth):

					if lookahead+counter < total:

						currentcolumn = lookahead+counter
						currentcolumnindex = (lookahead+counter) % displaypanelwidth
						#currentcolumnindex = displaypanelwidth - currentcolumnindex - 1
						#print "current column: " + str(currentcolumn) + "	column index: " + str(currentcolumnindex)  # display which column would currently be activated
						
						wpi.digitalWrite(cols[currentcolumnindex], LOW)  # turn on column

						#rowstring = "	row lights on: "
						for rowindex in outputpanellist[currentcolumn]:

							wpi.digitalWrite(rows[rowindex], HIGH)  # turn on row

							#rowstring += str(rowindex) + "  "

						time.sleep(columndisplaylength)

						wpi.digitalWrite(cols[currentcolumnindex], HIGH)  # turn off column

						## turn rows low
						for x in range(8):
							wpi.digitalWrite(rows[x], LOW)

						#print "light display column: " +  str(currentcolumnindex) + rowstring
					


			counter += 1
		#print number



##---Main---------------------------------------------------------------------#

def main():

	setup()  #function sets the pins for the program. Only ran once. 

	#for i in range(8):
	#	testcols(8-i-1)  # calculation will light columns from 7 to 0, with a 1 second pause between. 
	#	time.sleep(1)


	text = "HI, MY NAME IS EVAN!"

	outpanel = convertstringfordisplay(text)


	counterfunction(outpanel)
	
	#testconsoledemo()

	#scrollalphanumtest()

	# success

if __name__ == '__main__':
	status = main()
	sys.exit(status)
