import matplotlib.pyplot as plt
import random

times = 2000  # number of cycles
profits = [[1,-1], [-1, 1], [-1,1], [1, -1]] # matrix of profits
x0 = random.uniform(0, 1) # the beginning belief of player0
x1 = random.uniform(0, 1) # the beginning belief of player1
num = 0  #saving png/pdf images with the name “fictitious[num].png/pdf”
#if num = None, images won’t be saved


x0_values = []
x1_values = []

values = [x0_values, x1_values ]

for t in range(times):
	x0_values.append(x0)
	x1_values.append(x1)
	
	# decision of player0's act at time t
	if profits[0][0]*(1-x0)+profits[1][0]*x0 > profits[2][0]*(1-x0)+profits[3][0]*x0 :
		a0 = 0
	elif profits[0][0]*(1-x0)+profits[1][0]*x0 < profits[2][0]*(1-x0)+profits[3][0]*x0 :
		a0 = 1
	else :
		a0 = random.choice([0,1])
	
	# decision of player1's act at time t
	if profits[0][1]*(1-x1)+profits[2][1]*x1 > profits[1][1]*(1-x1)+profits[3][1]*x1 :
		a1 = 0
	elif profits[0][1]*(1-x1)+profits[2][1]*x1 < profits[1][1]*(1-x1)+profits[3][1]*x1 :
		a1 = 1
	else :
		a1 = random.choice([0,1])
	
	#updating beliefs
	x0 =  (a1 + x0*(t+1))/(t+2)
	x1 =  (a0 + x1*(t+1))/(t+2)
    
for i, j in enumerate(values):
    plt.subplot(2, 1, i+1)
    plt.hist(j, bins=50, label='x_'+str(i)+'(t)')
    plt.legend()
	
if num != None:
    plt.savefig('fictitious_hist' + str(num) + '.png')
    plt.savefig('fictitious_hist' + str(num) + '.pdf')

plt.show()