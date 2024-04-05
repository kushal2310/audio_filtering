import numpy as np
import matplotlib.pyplot as plt

# Given values of r(i), p(i), and k(i)
r_values = [0.05129142-0.14312607j, 
            0.06029142+0.15161107j, 
            -0.03024359+0.02138604j, 
            -0.07016319-0.02218603j]

p_values = [0.84375227+0.0434749j, 
            0.88462217-0.0355749j, 
            0.94324798+0.10465852j, 
            0.93221198-0.10386351j]

k_values = [3.20e-5, 0, 0, 0]

# Time indices
n_values = np.arange(31)  # n values up to 30

# Compute h(n)
hn_values = np.zeros_like(n_values, dtype=np.complex128)
for n in n_values:
    for i in range(len(r_values)):
        hn_values[n] += r_values[i] * (p_values[i] ** n)
    for j in range(len(k_values)):
        if n - j >= 0:
            hn_values[n] += k_values[j]

# Plot
plt.stem(n_values, np.abs(hn_values))
plt.xlabel('$n$')
plt.ylabel('$|h(n)|$')
plt.title('Magnitude of $h(n)$')
plt.grid(True)
plt.show()
