def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    elif(c>b and c>a):
        return c
    
a= int(input("Enter the value of  a: "))    
b= int(input("Enter the value of  b: "))    
c= int(input("Enter the value of  c: ")) 
print(greatest(a,b,c))  