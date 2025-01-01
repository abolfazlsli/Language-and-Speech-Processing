# Gradient Descent Optimization

This project implements a simple gradient descent algorithm to minimize a quadratic objective function. The goal is to demonstrate how gradient descent iteratively updates the variable to find the minimum of the function.

## Overview

The main components of this project include:

- **Objective Function**: A quadratic function \( f(x) = x^2 \) is defined as the function to be minimized.
- **Gradient Calculation**: The gradient of the objective function is computed, which is used to update the variable.
- **Gradient Descent Algorithm**: The algorithm iteratively updates the variable based on the gradient and a specified learning rate.
- **Visualization**: The history of updates to the variable is visualized using Matplotlib.

## Requirements

To run this project, you need to have the following Python packages installed:

- `numpy`
- `matplotlib`

You can install the required packages using pip:

```bash
pip install numpy matplotlib
```

## Code Explanation

### Functions

1. **`objective_function(x)`**: 
   - Defines the objective function \( f(x) = x^2 \).

2. **`gradient(x)`**: 
   - Computes the gradient of the objective function, which is \( f'(x) = 2x \).

3. **`gradient_descent(starting_point, learning_rate, num_iterations)`**: 
   - Implements the gradient descent algorithm.
   - Takes a starting point, learning rate, and number of iterations as input.
   - Updates the variable \( x \) based on the gradient and learning rate.
   - Records the history of \( x \) updates for visualization.

### Main Code Execution

- The starting point is set to 10.0, the learning rate is set to 0.1, and the number of iterations is set to 20.
- The `gradient_descent()` function is called to perform the optimization.
- The final point after the specified number of iterations is printed.

### Visualization

The history of updates to the variable \( x \) is plotted:
- The x-axis represents the iteration number.
- The y-axis represents the value of \( x \) at each iteration.
- The plot includes markers to indicate the updates.

### Visualization Code

```python
plt.plot(history, marker='o')
plt.title('History of x Updates')
plt.xlabel('Iteration Number')
plt.ylabel('Value of x')
plt.grid()
plt.show()
```

## Running the Code

To run the code, simply execute the script:

```bash
python gradient_descent.py
```

Make sure to replace `gradient_descent.py` with the actual filename if it's different.

## Conclusion

This project provides a basic implementation of the gradient descent optimization algorithm. It demonstrates how the algorithm iteratively updates a variable to minimize a quadratic function. You can experiment with different starting points, learning rates, and objective functions to see how they affect the convergence behavior.

Feel free to modify the code and explore further applications of gradient descent!