import numpy as np
v=float(input())
t=int(input())
s=108
if v>0:
    print(int((v*t)%s))

else:
    print(int(108-(abs(v)*t)%s))
pras='asdasd'