# Import libraries
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(14, 8))

# Creating histogram
samples = np.random.randn(10000)
plt.hist(samples, bins=30, density=True,
         alpha=0.5, color=(0.9, 0.1, 0.1))

# Add a title
plt.title('Random Samples - Normal Distribution')

# Add X and y Label
plt.ylabel('X-axis')
plt.ylabel('Frequency')

# Creating vectors X and Y
x = np.linspace(-4, 4, 100)
y = 1 / (2 * 3.14) ** 0.5 * np.exp(-x ** 2 / 2)

# Creating plot
plt.plot(x, y, 'b', alpha=0.8)

# Show plot
plt.show()









