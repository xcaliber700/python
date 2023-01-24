a=[0,1,2,3,4,5,2]
b=[2,5,4]
c=[]
for i in a:
	if i in b:
		c.append(i)
print(c)