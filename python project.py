a=int(input("Enter the starting Range: "))
b=int(input("Enter the Ending Range: "))
print(+"range is"+(",a,",",b,")")
c1=0 #count for prime numbers
c2=0 #count for composite numbers
print("Then the status of each number in the range is:")
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                print(i,"is a COMPOSITE NUMBER")
                c2=c2+1
                break
        else:
            print(i,"is a PRIME NUMBER")
            c1=c1+1
    elif i==0 or i==1:
        print(i,"is neither a prime nor a composite number")
    elif c<0:
        print(i,"is neither a prime nor a composite number")
    else:
        print(c,"is a COMPOSITE NUMBER")
        c2=c2+1
print("count:",c1,"prime","and",c2,"composite number in the range",a,"to",b)
