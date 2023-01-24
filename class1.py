class employee:
	companyname="chitkara"
	def __init__(self,eid,ename):
		self.ename=ename
		self.eid=eid
	def displayname(self):
		print(" ",self.ename)
	def displayid(self):
		print(" ",self.eid)

e1=employee(1,"darun")
e1.displayname()
e1.displayid()