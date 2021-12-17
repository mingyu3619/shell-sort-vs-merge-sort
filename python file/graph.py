import matplotlib.pyplot as plt
import  math
n=range(0,100)
#y=n**(1.5)
y=math.pow(n,1.5)
y1=n*math.log(n)
plt.plot(n,y,label="shell",ms=1)
plt.plot(n,y1,label="merge",ms=1)
#plt.plot(n,shell_memory,label='shell',ms=1)

plt.xlabel("Number of list element")
plt.ylabel("time(secs)")
plt.legend()
plt.show()