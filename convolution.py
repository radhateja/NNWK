import numpy as np

h=int(input("enter the input size:"))
print("input height & width:",int(h),"*",int(h))
k=int(input("enter the kernel size:"))
print("kernel height & width:",int(k),"*",int(k))
p=int(input("enter the padding size:"))
print("padding height & width:",int(p),"*",int(p))
s=int(input("enter the strides:"))
print("strides height & width:",int(s),"*",int(s))
p1=p2=p
o=h+p1+p2-k
out=(o/s)
out+=1
print(out)
if(out == h):
    print("output height & width:",int(out),"*",int(out))
else:
    print("This configuration not valid")
