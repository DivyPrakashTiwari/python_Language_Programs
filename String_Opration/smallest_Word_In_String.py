s=input("enter the string")
sp=s.split()
I=len(sp)
In=[]
for i in range(0,I):
    In.append(len(sp[i]))
m=1000
for i in range(0,I):
    if(m>int (In[i])):
        m=In[i]
        n=i
print("the smallest word is ",sp[n])