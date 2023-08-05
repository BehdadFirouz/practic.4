import math
i=1
nomber=int(input("yek adad tabiyi vared konid :       "))
while i<=nomber :
    j=math.factorial(i)
    if j==nomber:
        print("in adad factorial adad" ,i ,"hast")
        break 
    elif j>nomber :
        print("in adad factorial adadi nist")
        break
    else:
        i+=1