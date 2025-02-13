import matplotlib.pyplot as plt


S_20k = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99]
D_20k = [1.786, 1.500, 1.891, 1.584, 1.705, 1.608, 1.836, 1.779, 1.995, 2.428]

plt.scatter(S_20k, D_20k)
plt.title('Capacity Dimension vs. Stickiness Factor (N = 20000)')
plt.xlabel('Stickiness Factor')
plt.ylabel('Capacity Dimension')
plt.show()