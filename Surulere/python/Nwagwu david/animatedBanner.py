#PROGRAM WHICH DISPLAYS A MESSAGE(CODELAGOS) ON THE SCREEN 
#AND MAKES IT MOVE FROM LEFT TO RIGHT
#Name: Nwagwu david
#phone no: 08170741426
#NOTE:RUN THE PROGRAM ON FULLSCREEN AND WAIT FOR 50s TO SEE THE FULL EFFECT
from time import sleep
from os import system
from random import randint

#WIDTH OF THE COMPUTER CONSOLE
width = 78
#MESSAGE TO BE PRINTED
message="CODELAGOS"
printedWord=["","","","","","","",""]
running=True
count=0
#DICTIONARY WHICH STORES THE LETTES OF THE MESSAGE
letters={
        "C":["  ***",
             " *   ",
             "*    ",
             "*    ",
             "*    ",
             " *   ",
             "  ***"],
             
        "D":["***  ",
             "*  * ",       
             "*   *",       
             "*   *",       
             "*   *",   
             "*  * ",
             "***  "],
             
        "E":["*****",
             "*    ",       
             "*    ",       
             "*****",       
             "*    ",   
             "*    ",
             "*****"],
             
        "A":["  *  ",
             " * * ",       
             "*   *",       
             "*****",       
             "*   *",   
             "*   *",
             "*   *"],
             
        "L":["*    ",
             "*    ",       
             "*    ",       
             "*    ",       
             "*    ",   
             "*    ",
             "*****"],
             
        "G":["*****",
             "*    ",       
             "*    ",       
             "*  **",       
             "*   *",   
             "*   *",
             "*****"],
             
        "O":["*****",
             "*   *",       
             "*   *",       
             "*   *",       
             "*   *",   
             "*   *",
             "*****"],
             
        "S":["*****",
             "*    ",       
             "*    ",       
             "*****",       
             "    *",   
             "    *",
             "*****"]
          

}
#FILLING AN ARRAY WITH EACH ROW OF THE LETTERS TO BE PRINTED
for row in range(7):
	for letter in message:
		printedWord[row]+=(str(letters[letter][row])+" ")
	
#OFFSET IS THE DISTANCE OF THE SCREEN FROM LEFT TO RIGHT INITIAL THE CONSOLE WON'T SHOW ANYTJING
offset=width

#BLINK DISPLAYS THE MESSAGE IN A CERTAIN POINT ON THE SCREEN AND THEN MOVES IT AGAIN TO ANOTHER POINT ON THE SCREEN
def blink():
	system("cls")
	offset=randint(0,26)
	mainRow= randint(0,30)
	for row in range(30):
		
		if row==mainRow:
			for Row in range(7):
				print(" "*offset,printedWord[Row][0:width-offset])
		else:
			print(" "*offset)
			
	sleep(5.0)
	

			
while running:
	system("cls")
	#STARTS PRINTING THE MESSAGE FROM LEFT TO RIGHT
	for row in range(7):
		print(" "*offset,printedWord[row][max(0,offset*(-1)):width-offset])
	
	offset -=1
	if offset<=(len(message)*7)*-1:
		offset=width
		count+=1
	#STARTS MOVING THE MESSAGE FROM ONE POINT ON THE SCREEN TO ANOTHER
	if count==3:
		for i in range(3):
			blink()
		count=0
	sleep(0.05)	

		
