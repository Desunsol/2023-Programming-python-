import string

def uj_tt(s) :
	s = s.replace('\n','')
	words = s.split()
	result = []
	
	j = 0
	for w in words :
		
		if j != 0 :
			result.append(' ')
		
		i = 0
		while i<len(w) :
			c = w[i:i+1]
			if c.isalnum() or (c in string.printable) or i+1 == len(w) :
				i = i + 1
			else :
				c = w[i:i+2]
				i = i+2
				
			result.append(c)
		j = j + 1
		
	return result
	

while True :
	sss1 = raw_input("input Korean sentence : ")
	sss2 = uj_tt(sss1)
	for t in sss2 :
		print t

