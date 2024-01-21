import matplotlib.pyplot as plt
from math import factorial
from datetime import datetime
 
n = int(input('How many lines?'))
 
linesX = []
timeY = []
starttime = datetime.now()
 
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()
    linesX.append(i + 1)
    timeY.append((datetime.now() - starttime).total_seconds() *1000) # Time delta in milliseconds
 
 
plt.scatter(linesX, timeY)
plt.ylabel('Time (ms)')
plt.xlabel('Row count')
plt.title('Pascal\'s Triangle Size Versus Runtime')
plt.show()