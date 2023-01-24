f=0
x=int(input("enter value:"))
for i in range(2,int(x/2)):
	if x%i==0:
		f=1
		break
if f==1:
	print("not prime")
else:
	print("prime")
