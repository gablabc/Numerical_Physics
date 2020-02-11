import matplotlib.pyplot as plt
import numpy as np
from finite_diff_1d_laplace import solveFiniteDiff
from scipy.integrate import trapz

# Add latex support for the graphs
from matplotlib import rc
rc('font',**{'family':'serif', 'serif':['Palatino'], 'size':12})
rc('text', usetex=True)

# Plot a single graph
x, f = solveFiniteDiff(conditions = [['dirichlet', 0], ['newmann', 1]])
plt.figure(1)
plt.plot(x, f)
plt.plot(x, x ** 3 / 3)
plt.xlabel(r'x')
plt.ylabel(r'f(x)')
plt.title(r'Solutions $\frac{d^2f}{dx^2} = -2x$ with $N = 100$')
plt.savefig("../../images/finite_diff/sol_1d_laplace.png")
plt.legend(['numerical', 'analytical'])

# Plot error for multiple N
N = np.logspace(1, 3).astype(int)
errors = np.zeros((N.shape))

for i in range(N.size):
    x, f = solveFiniteDiff(N = N[i], conditions = [['dirichlet', 0], ['newmann', 1]])
    errors[i] = trapz(np.abs(x**3 / 3 - f), dx = 1 / N[i])

plt.figure(2)
plt.loglog(N, errors)
plt.xlabel(r"N")
plt.ylabel(r"error $L_1$")
plt.title(r'error $L_1$ as a function of discretization')
plt.savefig("../../images/finite_diff/error_1d_laplace.png")

# show both figures
plt.show()