from sys import argv
import os

filename=argv[1]
os.system("python symbolTable.py "+str(filename))
os.system("python litTab1.py "+str(filename))
os.system("python IntMed.py "+str(filename))
os.system("python Lst.py")
	
