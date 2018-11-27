from Register import *
from Instructions import *
from sys import argv

literal=[]
lineCount=[]
literalValue=[]
lit=[]
lc1=[]
symval=[]
reg=Reg32.keys()
literals=[]
lc=[]
litVal=[]
symbol=[]
def symLiteral():
	token_list=[]
	fp=open("symbol_table.txt","r+")
	stri=""
	n1=[]
	
	for lines in fp.readlines():	
		token_list=lines.split('\t')
		len1=len(token_list)
		if(token_list[5]=='S'):
				symbol.append(token_list[2])
				lc1.append(token_list[1])
				lit.append(token_list[2])
				varr=token_list[len1-1]
				if(',0' in varr):
					vr=varr.split(',0')
					valx=convert(vr[0])
					valx.append('00')
					if(',0,10' in varr):
						valx.append('000A')
				        symval.append(''.join(valx))
					
				elif(',' in varr):
					n=varr.split(',')
					for p in range(len(n)):
						n1.append(hex(int(n[p])).upper())
					symval.append(','.join(n1))
				elif(varr[0].isdigit()):
					valx=hex(int(varr)).upper()
					symval.append(valx)
					
	

						
def instLiteral(filename):
	linecount=0
	token=[]
	valTokens=[]
	address_access=['dword','byte','qword']
	reg=Reg32.keys()
	fa=open(filename,"r+")
	for line in fa.readlines():
		linecount+=1
		token=line.split()
		
		for i in range(len(token)):
			if token[i] in literal_instr:
				#print("is instruction"+str(token[i]))
				valTokens=(token[i+1]).split(',')
				if(len(valTokens)>=2):
					for j in range(len(valTokens)):		
						if('[' in valTokens[j]):
							variable=valTokens[j].split('[')
							if(variable[0] in address_access):
								sym=variable[1].strip(']')
								if(sym in reg) or (sym in symbol):
										continue
						elif((valTokens[j] not in symbol) and (valTokens[j] not in reg)):
								valTokens[j]=valTokens[j].strip('\'')
								literals.append(valTokens[j])
								lc.append(linecount)
								if(valTokens[j].isdigit()):
									val=hex(int(valTokens[j]))
								else:
									val=hex(ord(valTokens[j]))
								litVal.append(val)
					

def convert(num):
	hexvalue=[]
	if(isinstance(num,str)):
		for i in range(len(num)-1):
			if(num[i]=='\"'):
				continue
			else:
				val=hex(ord(num[i]))
				hexlist=val.split('x')
				hexvalue.append(hexlist[1].upper())
		return(hexvalue)
	elif(isinstance(num,char)):
		return(hex(ord(num)))
	else:
		return(hex(num))






def combine():
	literal.append(lit)	
	literal.append(literals)
	lineCount.append(lc1)
	lineCount.append(lc)
	literalValue.append(symval)
	literalValue.append(litVal)
	

def write_to_file():	
	f=open("literal_table.txt","w+")
	counter=0
	for i in range(len(literal)):
		for j in range(len(literal[i])):
			f.write(str(counter)+"\t"+str(lineCount[i][j])+"\t"+str(literal[i][j])+"\t"+str(literalValue[i][j])+"\n")		
			counter+=1


	print("File written successfully\n")

	

def literalTable(filename):
	symLiteral()
	instLiteral(filename)
	combine()

if __name__ == '__main__':
    filename=argv[1]
    
    literalTable(filename)
    write_to_file()
