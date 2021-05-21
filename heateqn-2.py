import numpy as np
import matplotlib.pyplot as plt

## Heat Equation via Crank-Nicolson method:
# Parameters
dt = 0.01
M = 20     # Number of time steps
dx = 0.01
N = 100    # Number of grid points

# Define the domain and initial Condition
x = np.linspace(dx/2,dx*(N-1/2),N)
u = np.cos(13*np.pi*x) + np.cos(7*np.pi*x) - 3*np.cos(2*x)

# Crank-Nicolson is an implicit scheme where B*u_{t+dt} = A*u_{t}
r = dt/(2*dx**2)
v = np.ones(N)
v[0] = 1/2
v[N-1] = 1/2
B = - np.diag(r*np.ones(N-1),1) - np.diag(r*np.ones(N-1),-1) + np.diag(1+2*r*v)
A = np.diag(r*np.ones(N-1),1) + np.diag(r*np.ones(N-1),-1) + np.diag(1-2*r*v)
E = []
t = []

plt.style.use('dark_background')

fig, [ax1,ax2] = plt.subplots(1,2)
for j in range(M):
    # Plot the results
    with plt.style.context('dark_background'):
        ax1.plot(x,u)

    # Comute Dirichlet Energy
    Du = (u[1:N]-u[0:N-1])/(dx)
    E.append(dx*sum(Du ** 2))
    t.append(dt*j)
    with plt.style.context('dark_background'):
        ax2.plot(t,E)

    # Update u
    f = np.matmul(A,u)
    u = np.linalg.solve(B,f)
plt.show()
# Reference:
# LeVeque, Randall J., 2007
