"""#1) one dimensional array
import numpy as np
marks= np.array([50,45,90])
print (marks)

#2) sequential one dimensional array
import numpy as np
a= np.arange(10,101,10)
print (a)

#3) one dimensional array with 5 random floating-point no. between 0 to 1
import numpy as np
b= np.random.random(5)
print (b)

#4) two dimensional array :2*3 with random int value less than 20
import numpy as np
c= np.random.randint (20, size=(2,3))
print (c)

#5) two dimensional array :2*3 with all the values as 1
import numpy as np
c= np.ones ((2,3))
print (c)


import matplotlib.pyplot as plt
vehicles= [10,20,25,35,40,45,52,60,70,75,80,90]
pollution= [30,40,17,59,40,50,30,60,20,90,10,45]
plt.scatter(vehicles, pollution, color= 'blue', marker= 's')
plt.xlabel('number of vehicles on roal')
plt.ylabel('air pllution levels (aqi)')
plt.title ('number of vehicles vs air pollution')
plt.show()"""


