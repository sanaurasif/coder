text=str(input("Enter Your Text :"))
count=len(text)
real=0
code=""
while real<count:
	c=text[real]
	if c=="a" or c=="A":
		d="2¹"
	elif c=="b" or c=="B":
		d="2²"
	elif c=="c" or c=="C":
		d="2³"
	elif c=="d" or c=="D":
		d="3¹"
	elif c=="e" or c=="E":
		d="3²"
	elif c=="f" or c=="F":
		d="3³"
	elif c=="g" or c=="G":
		d="4¹"
	elif c=="h" or c=="H":
		d="4²"
	elif c=="i" or c=="I":
		d="4³"
	elif c=="j" or c=="J":
		d="5¹"
	elif c=="k" or c=="K":
		d="5²"
	elif c=="l" or c=="L":
		d="5³"
	elif c=="m" or c=="M":
		d="6¹"
	elif c=="n" or c=="N":
		d="6²"
	elif c=="o" or c=="O":
		d="6³"
	elif c=="p" or c=="P":
		d="7¹"
	elif c=="q" or c=="Q":
		d="7²"
	elif c=="r" or c=="R":
		d="7³"
	elif c=="s" or c=="S":
		d="7⁴"
	elif c=="t" or c=="T":		
		d="8¹"
	elif c=="u" or c=="U":
		d="8²"
	elif c=="v" or c=="V":
		d="8³"
	elif c=="w" or c=="W":
		d="9¹"
	elif c=="x" or c=="X":
		d="9²"
	elif c=="y" or c=="Y":
		d="9³"
	elif c=="z" or c=="Z":
		d="9⁴"
	else:
		d="c"
	main=code+d
	code=main
	real+=1
print(main)
	
	