def circle(r):
	a=3.14*r*r
	return (a,r)

r=int(input("enter radius:"))
x=circle(r)
print("area=",x)