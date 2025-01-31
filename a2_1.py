import sys

cipher = input()
sum=0

if not cipher.isdigit():
  sys.exit()
  
for i in range (len(cipher)):
    sum+=int(cipher[i])

if len (cipher)!=4:
    print("INVALID INPUT")
    sys.exit()
for i in range (len(cipher)):
    if cipher[i]=="0":
        print ("INVALID INPUT")
        sys.exit()
    for j in range (i+1,len(cipher)):
        if sum//int(cipher[j])==sum//int(cipher[i]):
            print ("INVALID INPUT")
            sys.exit()

inp=0
directions=[]
steps=[]
north, south, east, west = [sum//int(cipher[i]) for i in range (4)]

while inp < 12:
    if inp%2==0:
        x=int(input())
        if x not in [north, south, east, west]:
            print ("INVALID INPUT")
            sys.exit()
        else:
            directions.append(x)
        inp+=1
    else:
        steps.append(int(input()))      
        inp+=1

x,y=0,0
for i in range(len(directions)):
    if directions[i]==north:
        y+=steps[i]
    elif directions[i]==south:
        y-=steps[i]
    elif directions[i]==east:
        x+=steps[i]
    elif directions[i]==west:
        x-=steps[i]
    else:
        pass
        
print(f"({x}, {y})")
