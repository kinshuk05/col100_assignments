n=int(input())

x,y=int(input()), int(input())

x+="0"*(max(len(x),len(y))-len(x))+str(x)
y+="0"*(max(len(x),len(y))-len(y))+str(y)

carry,sum=0,""

for i in range (-1,min(-len(x),-len(y))-1,-1):
    sum+=str((carry+int(x[i])+int(y[i]))%n)
    carry+=(carry+int(x[i])+int(y[i]))//n
  
print(sum)
