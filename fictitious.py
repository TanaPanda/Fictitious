import matplotlib.pyplot as plt
import random

times = 100
profits = [[1,-1], [-1, 1], [-1,1], [1, -1]]
x0 = random.uniform(0, 1)
x1 = random.uniform(0, 1)

x0_values = []
x1_values = []

for t in range(times):
	x0_values.append(x0)
	x1_values.append(x1)
	
	if profits[0][0]*(1-x0)+profits[1][0]*x0 > profits[2][0]*(1-x0)+profits[3][0]*x0 :
		a0 = 0
	elif profits[0][0]*(1-x0)+profits[1][0]*x0 < profits[2][0]*(1-x0)+profits[3][0]*x0 :
		a0 = 1
	else :
		a0 = random.choice([0,1])
		
	if profits[0][1]*(1-x1)+profits[2][1]*x1 > profits[1][1]*(1-x1)+profits[3][1]*x1 :
		a1 = 0
	elif profits[0][1]*(1-x1)+profits[2][1]*x1 < profits[1][1]*(1-x1)+profits[3][1]*x1 :
		a1 = 1
	else :
		a1 = random.choice([0,1])
	
	x0 =  (a1 + x0*(t+1))/(t+2)
	x1 =  (a1 + x1*(t+1))/(t+2)

plt.plot(x0_values, 'b-', label = 'x_0(t)')
plt.plot(x1_values, 'r-',  label = 'x_1(t)')
plt.legend()
plt.show()