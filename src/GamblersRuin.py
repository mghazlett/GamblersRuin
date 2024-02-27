import numpy as np

transition_matrix = np.zeros([15,15]) #make a matrix of zeros that is 15 x 15. 

#tuples work for indices
transition_matrix[(0,0)] = 1  #prob of transitioning out of losing state (at the beginning)
transition_matrix[(14,14)] = 1 #prob of transitioning out of losing state (at the end)
p = 17/36 #probablilty of winning a hand.
#women you liang ge terminal states: (0,0) he (14,14) 

for i in range(1,14):
    transition_matrix[i,i-1] = 1-p
    transition_matrix[i,i+1] = p 

#representing state
state = np.zeros([15])
state[4] = 1 #this means you are starting with $500. because $500 is in the 4th idx. 

# code golf -- fewest chars
#mapping
map = np.append([0,150,350], np.append(450,1050,50))
# dollar_amt = np.array([0,50,350]) #this is how I did it. above is katherine's, it's shorter
# dollar_amt.append([np.arange(450,1050,50)])

#we need to transform the arrays into matrices so we can math 
transition_matrix = np.matrix(transition_matrix)
state = np.matrix(state).T #.T = transpose
#how do we know where we are in the second round
second_round_state = transition_matrix * state
third_round_state = transition_matrix * second_round_state
fiftieth_round_state = transition_matrix**49 * state

print(second_round_state)
print(fiftieth_round_state)
