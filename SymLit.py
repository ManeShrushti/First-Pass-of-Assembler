symlist={}
literal={}
labellist={}
symvalue={}
def getsymbols():
	fa=open("symbol_table.txt",'r+')
	for line in fa.readlines():
		value=line.split('\t')
		if(value[5]=='S'):
			symlist[value[2]]=value[0]
		else:
			labellist[value[2]]=value[0]
	fa.close()
			
		
def getliterals():
	fl=open("literal_table.txt",'r+')
	for line in fl.readlines():
		value=line.split('\t')
		literal[value[2]]=value[0]
		v=value[3].split('\n')
		symvalue[value[2]]=v[0]
	fl.close()


def getsymbolNames():
	fa=open("symbol_table.txt",'r+')
	for line in fa.readlines():
		value=line.split('\t')
		if(value[5]=='S'):
			symlist[value[0]]=value[2]
		else:
			labellist[value[0]]=value[2]
	fa.close()

def getliteralsNames():
	fl=open("literal_table.txt",'r+')
	for line in fl.readlines():
		value=line.split('\t')
		literal[value[0]]=value[2]
		v=value[3].split('\n')
		symvalue[value[0]]=v[0]
	fl.close()


			
		
