nterm=int(input("Enter Number : "))
n1,n2=0,1
count=0
if (nterm<=0):
    print("Enter Positive")
elif (nterm==1):
    print("Series Of ",nterm," :")
    print(n1)
else:
    print("Series")
    while count<nterm:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1