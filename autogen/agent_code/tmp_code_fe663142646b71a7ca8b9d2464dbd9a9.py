import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[1,2,3,4,5]

plt.scatter(x, y)
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')

plt.savefig('scatter_plot.png')