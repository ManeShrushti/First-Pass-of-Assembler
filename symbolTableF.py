from sys import argv
import sys
from Register import *
from Instructions import *
	
symName=[]
symSize=[]
list1=[]
symVal=[]
data_type=[]
data_size=[]
store_size=[]
symbol_tag=[]
addr=[]
value=[]
global line_count
linecount=[]
defined_label=[]
def symbolTable(filename):
	
	extern_list=[]
	token_list=[]
	sym=""
	size=0
	ind=0
	sumlen=0
	f=open(filename,"r")
	datakeys=data.keys()
	bsskeys=bss.keys()
	line_count=0
	vs=[]
	for str1 in f.readlines():
		line_count+=1
		token_list=str1.split()
		for i in range(len(token_list)):
			if(token_list[i] in datakeys):
				size1=data.get(token_list[i])
				symName.append(token_list[i-1])
				symSize.append(size1)
				symbol_tag.append("S")
				data_type.append('D')
				symVal=token_list[i+1].split(",")
				for k in range(len(symVal)):			
					vs.append(symVal[k])
				value.append(','.join(vs))
				data_size.append(len(symVal))
				v=len(symVal)

				if(v==0):
					store_size.append(size1)
				else:
					store_size.append((v)*size1)
				linecount.append(line_count)

			elif(token_list[i]=='db'):
				arr=[]
				arr1=[]
				symName.append(token_list[i-1])
				symSize.append(2)
				symbol_tag.append("S")
				data_type.append('D')
				i+=1
				symVal=token_list[i]
				sumlen=0
				while((symVal.find(',0'))== -1):
					arr.append(symVal)
					arr.append(" ")
					i+=1
					symVal=token_list[i]
					sumlen+=(len(symVal)-1)

				arr.append(token_list[i])	
				sumlen+=(len(token_list[i]))
				value.append(arr)
				data_size.append(sumlen)
				v=sumlen

				store_size.append(v)
				linecount.append(line_count)
	
			elif(token_list[i]=='equ'):
				symName.append(token_list[i-1])
				symSize.append(1)
				symbol_tag.append("S")
				data_type.append('D')
				symVal=token_list[i+1].split("$-")
				if(symVal in symName):
					ind=symName.index(symVal)			
				value.append(str(data_size[ind]))
				data_size.append(4)
				v=len(value[ind])
				store_size.append(4*v)
				linecount.append(line_count)


			elif(token_list[i] in bsskeys):
				size=bss.get(token_list[i])
				symName.append(token_list[i-1])
				symSize.append(size)
				symbol_tag.append("S")
				data_type.append('D')

				symVal=int(token_list[i+1])*size
				value.append(token_list[i+1])
				data_size.append(int(token_list[i+1]))
				store_size.append(symVal)
				linecount.append(line_count)

			elif(token_list[i]=='extern'):
				extern_list=token_list[i+1].split(',')

			elif(token_list[i] in label_set):
				if token_list[i+1] not in defined_label:
					symName.append(token_list[i+1])
					symbol_tag.append('L')
					symSize.append('-')
					data_size.append('-')
					store_size.append(0)
					value.append('-')
					linecount.append(line_count)
					defined_label.append(token_list[i+1])
					data_type.append('U')
								

			elif(':' in token_list[i]):
					sym=token_list[i].split(':')
					val=sym[0]
					if (not(val in defined_label)):
						symName.append(val)
						symbol_tag.append('L')
						symSize.append('-')
						data_size.append('-')
						value.append('-')
						data_type.append('D')
						store_size.append(0)
						defined_label.append(val)
						linecount.append(line_count)	
	
	addr.append(0)		
	for i in range(len(store_size)-1):
		if(symName[i+1]=='main'):
			addr.append(0)
		elif((int(store_size[i]))==0):
			addr.append(0)
		else:
			addr.append((int(addr[i]))+(int(store_size[i])))
	
def write_to_file():	

	f1=open("symbol_table.txt","w")
	count=0
	for x in range (len(symName)):
		str1=""
		f1.write(str(count)+ "\t"+str(linecount[x])+"\t"+symName[x] +"\t" + str(symSize[x]) +"\t"+ str(data_size[x]) + "\t" + str(symbol_tag[x]) + "\t" + str(data_type[x])+ "\t"+str(addr[x])+ "\t" + str1.join(value[x])+"\n")
		count+=1
	print("Written to file successfully")
	f1.close()


if __name__ == '__main__':
    filename=argv[1]
    
    symbolTable(filename)
    write_to_file()
