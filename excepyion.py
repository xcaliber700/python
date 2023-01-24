def findDivide(a,b):
    c=[]
    j=0
    for x in a:
            if(j==(len(b))):
                break
            try:
                # TODO: write code...
                value=x/b[j]
                c.append(value)
            except ZeroDivisionError:
                print("Zero Division Error")
            j=j+1
    print(c)
    
    
    
    
    
    
a=[2,3,4,5,6]
b=[2,0,5,6.8]
findDivide(a,b)