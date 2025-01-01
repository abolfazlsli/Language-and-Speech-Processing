import numpy as np
import matplotlib.pyplot as plt

def objective_function(x):
    return x**2

def gradient(x):
    return 2*x

def gradient_descent(starting_point, learning_rate, num_iterations):
    x = starting_point
    history = [x]
    
    for _ in range(num_iterations):
        grad = gradient(x)
        x = x - learning_rate * grad
        history.append(x)
    
    return x, history

starting_point = 10.0
learning_rate = 0.1 
num_iterations = 20 

final_x, history = gradient_descent(starting_point, learning_rate, num_iterations)

print("Final point:", final_x)

plt.plot(history, marker='o')
plt.title('History of x Updates')
plt.xlabel('Iteration Number')
plt.ylabel('Value of x')
plt.grid()
plt.show()
