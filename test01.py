import sys
import os
import time


i = 0
j = 0
s = " "
while i==0 :

	print (s+"    *")
	print (s+" * * * *")
	print (s+"  * * *")
	print (s+" *     *")

	time.sleep(0.07)
	
	os.system('cls')
	
	if (j%10 > 5) :
		s = s[0:len(s)-2]
	else :
		s = s + " "
	
	j = j + 1
	
