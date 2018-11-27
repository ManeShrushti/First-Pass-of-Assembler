from sys import argv
import sys
from Register import *
from Instructions import *
from SymLit import *

op=[]
line_count=0
flag=0
token=[]
fi=open("Intmed.txt","w")
def func(n):
	global line_count
	global flag
	global op
	global token
	if(op[0] in Reg32 and op[1] in Reg32):
		fi.write(str(line_count)+"\t\t"+str(token[n])+ " " + Reg32.get(op[0]) + " " +Reg32.get(op[1]))
		flag=1
	elif(op[0] in Reg16 and op[1] in Reg16):
		fi.write(str(line_count)+"\t\t"+str(token[n])+ " " + Reg16.get(op[0]) + " " +Reg16.get(op[1]))
		flag=1
	elif(op[0] in Reg8 and op[1] in Reg8):
		fi.write(str(line_count)+"\t\t"+str(token[n])+ " " + Reg8.get(op[0]) + " " +Reg8.get(op[1]))
		flag=1
	elif(op[0] in Reg32 and op[1] in symlist):
		fi.write(str(line_count)+"\t\t"+str(token[n])+ " " + Reg32.get(op[0]) + " #Sym" +symlist.get(op[1]))
		flag=1
	elif(op[0] in Reg16 and op[1] in symlist):
		fi.write(str(line_count)+"\t\t"+str(token[n])+ " " + Reg16.get(op[0]) + " #Sym" +symlist.get(op[1]))
	elif(op[0] in Reg8 and op[1] in symlist):
		fi.write(str(line_count)+"\t\t"+str(token[n])+ " " + Reg8.get(op[0]) + " #Sym" +symlist.get(op[1]))
		flag=1
	elif(op[0] in symlist and op[1] in Reg32):
		fi.write(str(line_count)+"\t\t"+str(token[n])+ "#Sym" + symlist.get(op[0]) + " " +Reg32.get(op[1]))
		flag=1
	elif(op[0] in symlist and op[1] in Reg16):
		fi.write(str(line_count)+"\t\t"+str(token[n])+ "#Sym" + symlist.get(op[0]) + " " +Reg16.get(op[1]))
		flag=1
	elif(op[0] in symlist and op[1] in Reg8):
		fi.write(str(line_count)+"\t\t"+str(token[n])+ "#Sym" + symlist.get(op[0])+ " " +Reg8.get(op[1]))
		flag=1
	elif(op[0] in Reg32 and op[1] in literal):
		fi.write(str(line_count)+"\t\t"+str(token[n])+ " " + Reg32.get(op[0]) + " Lit#" +literal.get(op[1]))
		flag=1
	elif(op[0] in Reg16 and op[1] in literal):
		fi.write(str(line_count)+"\t\t"+str(token[n])+ " " + Reg16.get(op[0]) + " Lit#" +literal.get(op[1]))
		flag=1
	elif(op[0] in Reg8 and op[1] in literal):
		fi.write(str(line_count)+"\t\t"+str(token[n])+ " " + Reg8.get(op[0]) + " Lit#" +literal.get(op[1]))
		flag=1



def intermediate(filename):
	
	data['db']=[1]
	f=open(filename,"r")
	getsymbols()
	getliterals()
	global line_count
	global flag
	global token
	global op
	for str1 in f.readlines():
		line_count+=1
		token=str1.split()	
		flag=0
		
		for i in range(len(token)):
			if token[i] in data:	
				
				if (token[i-1] in symlist) and (token[i-1] in literal):
					fi.write(str(line_count)+"\t\tSym#"+ str(symlist.get(token[i-1])) + " "+str(token[i])+ " " + symvalue[token[i-1]])				
					flag=1
					
			elif token[i] in bss:
				if(token[i-1] in symlist) and (token[i-1] in literal):
					
					fi.write(str(line_count)+"\t\tSym#"+ str(symlist.get(token[i-1]))+ " "+ str(token[i])+" "+ symvalue[token[i-1]])				
					flag=1
					
			elif token[i] in instruction:
				if(',' in token[i+1]):
					op=token[i+1].split(',')
					if(len(op)>1):
						if(token[i]=='cmp'):
							if('byte[' in op[0] or 'dword['in op[0]):
								byte=op[0].split('[')
								b=byte[1].split("]")
								if(b[0] in Reg32 and op[1] in literal):
									fi.write(str(line_count)+"\t\t"+str(token[i])+ " " +byte[0] +"["+ Reg32.get(b[0]) + "] Lit#"+ literal.get(op[1])) 				
									flag=1
								elif(b[0] in Reg16 and op[1] in literal):
									fi.write(str(line_count)+"\t\t"+str(token[i])+ " " +byte[0] +"["+ Reg16.get(b[0]) + "] Lit#"+ literal.get(op[1])) 				
									flag=1
								if(b[0] in Reg8 and op[1] in literal):
									fi.write(str(line_count)+"\t\t"+str(token[i])+ " " +byte[0] +"["+ Reg8.get(b[0]) + "] Lit#"+ literal.get(op[1])) 				
									flag=1
						elif(token[i]=='mov'):
							if('byte[' in op[1] or 'dword['in op[1]):
								
								byte=op[1].split('[')
								b=byte[1].split("]")
								if(b[0] in Reg32 and op[0] in Reg32):
									fi.write(str(line_count)+"\t\t"+str(token[i])+ " " + Reg32.get(op[0])+" "+byte[0] +"["+ Reg32.get(b[0]) + "] ") 	
									flag=1
								if(b[0] in literal and op[0] in Reg32):
									fi.write(str(line_count)+"\t\t"+str(token[i])+ " " + Reg32.get(op[0])+" "+byte[0] +"[Lit#"+ literal.get(b[0]) + "] ") 	
									flag=1	
							else:
								func(i)		
						else:	
							func(i)
						
					
				else:
					if(token[i+1] in Reg32):
						flag=1	
						fi.write(str(line_count)+"\t\t"+str(token[i])+ " " + Reg32.get(token[i+1]))
					elif(token[i+1] in Reg16):
						flag=1						
						fi.write(str(line_count)+"\t\t"+str(token[i])+ " " + Reg16.get(token[i+1]))
					elif(token[i+1] in Reg8):
						flag=1
						fi.write(str(line_count)+"\t\t"+str(token[i])+ " " + Reg8.get(token[i+1]))
					elif token[i+1] in labellist:
						flag=1
						fi.write(str(line_count)+"\t\t"+str(token[i])+ " Label#" + str(labellist.get(token[i+1])))
					elif token[i+1] in literal:
						flag=1
						fi.write(str(line_count)+"\t\t"+str(token[i])+ " Lit#" + str(literal.get(token[i+1])))
		if(flag==0):
			if(':' in str1):
				string=str1.split(':')
				if(string[0] in labellist):
					fi.write(str(line_count)+"\tLabel#"+str(labellist.get(string[0])+ ":"))
			else:		
				string=str1.split('\n')
				fi.write(str(line_count)+"\t"+str(string[0]))
		fi.write("\n")
		

if __name__ == '__main__':
    filename=argv[1]
    intermediate(filename)
