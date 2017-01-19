
import sys

def counterfunction():

	scrolliterations = 10
	columndisplayiterations = 10
	displaypanelwidth = 8
	outputpanellist = [[0, 1, 2, 3, 4, 5, 6, 7], [3], [3], [0, 1, 2, 3, 4, 5, 6, 7], [], [], [0, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 7], [], [], [7], [5, 6], [], [], [], [], [0, 1, 2, 3, 4, 5, 6, 7], [1], [1], [0, 1, 2, 3, 4, 5, 6, 7], [], [], [0, 1, 2], [3, 4, 5, 6, 7], [0, 1, 2], [], [], [], [], [0, 1, 2, 3, 4, 5, 6, 7], [0], [0], [1, 2, 3, 4, 5, 6, 7], [], [], [1, 2, 3, 4, 5, 6, 7], [0, 1, 4], [0, 1, 4], [1, 2, 3, 4, 5, 6, 7], [], [], [0, 1, 2, 3, 4, 5, 6, 7], [1], [1], [0, 1, 2, 3, 4, 5, 6, 7], [], [], [0, 1, 2, 3, 4, 5, 6, 7], [0, 3, 7], [0, 3, 7], [0, 7], [], [], [], [], [0, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 7], [], [], [1, 2, 7], [0, 3, 7], [0, 3, 7], [0, 3, 4, 5, 6], [], [], [], [], [0, 1, 2, 3, 4, 5, 6, 7], [0, 3, 7], [0, 3, 7], [0, 7], [], [], [0, 1, 2, 3, 4, 5], [6, 7], [6, 7], [0, 1, 2, 3, 4, 5], [], [], [1, 2, 3, 4, 5, 6, 7], [0, 1, 4], [0, 1, 4], [1, 2, 3, 4, 5, 6, 7], [], [], [0, 1, 2, 3, 4, 5, 6, 7], [0], [0], [1, 2, 3, 4, 5, 6, 7], [], [], [0, 1, 2, 3, 4, 5, 7], [], []]

	
	total = len(outputpanellist)  # the length 

	## times to fully scroll 
	## uncomment below to scroll thru entire message until interrupted
	# while True:
	for number in range(scrolliterations):
		counter = 0

		## iterate thru the full panellist
		while counter < total:

			print "list index counter: " + str(counter)

			## number of repeating iterations thru the display panel
			for repeatdisplay in range(columndisplayiterations):

				## range of numbers in the list to count ahead, look ahead
				for lookahead in range(displaypanelwidth):

					if lookahead+counter < total:

						currentcolumn = lookahead+counter
						currentcolumnindex = (lookahead+counter) % displaypanelwidth

						print "current column: " + str(currentcolumn) + "	column index: " + str(currentcolumnindex)  # display which column would currently be activated
					
						rowstring = "	row lights on: "
						for rowindex in outputpanellist[currentcolumn]:

							   rowstring += str(rowindex) + "  "

						print "light display column: " +  str(currentcolumnindex) + rowstring
					


			counter += 1
		print number




def main():

	counterfunction()

	# success

if __name__ == '__main__':
	status = main()
	sys.exit(status)

