import matplotlib.pyplot as plt
import numpy as np
import math


def get_force(G, m, M, r):
    return -r*(G*m*M)/(np.linalg.norm(r)**3)
def get_potential(G,m,M,r):
    return -1*G*m*M/np.linalg.norm(r)

def propagate_euler(dt,r,v,m,G,M):
    new_r = r+v*dt+(dt**2)*0.5*get_force(G,m,M,r)/m
    new_v = v+dt*get_force(G,m,M,r)/m
    return [new_r,new_v]

def propagate_verlet(dt, r, r_prev, m, G,M):
    new_r = 2*r -r_prev + (get_force(G,m,M,r)/m)*dt*dt
    return new_r


def propagate_frog(dt,r, v, m, G, M):
    new_v = v + get_force(G,m,M,r)*dt/m
    new_r = r+new_v*dt
    results = [new_r, new_v]
    return results

T=30000
pot_traj = np.empty((T-1,1 ))
kin_traj = np.empty((T-1,1))
total_traj = np.empty((T-1,1))


G=0.01
M=500
dt=0.001
m=0.1

r_traj = np.empty((T,2))
v_traj = np.empty((T,2))
r_traj[0] = np.array([2.0,0.0])
v_traj[0] = np.array([0.0,0.1/m])
for i in range(T-1):
    results = propagate_euler(dt, r_traj[i], v_traj[i], m, G, M)
    r_traj[i+1] = results[0]
    v_traj[i+1] = results[1]
    pot_traj[i] = get_potential(G,m,M,r_traj[i])
    kin_traj[i] = 0.5*m*(np.linalg.norm(v_traj[i])**2)
    total_traj[i] = pot_traj[i] + kin_traj[i]

plt.plot(r_traj[:,0],r_traj[:,1])
plt.show()
plt.plot(pot_traj)
plt.plot(kin_traj)
plt.plot(total_traj)
plt.show()


start=propagate_euler(dt, r_traj[0], v_traj[0], m, G, M)
r_traj[1] = start[0]

for i in range(1,T-1):
    r_traj[i+1] = propagate_verlet(dt, r_traj[i], r_traj[i-1], m, G, M)

plt.plot(r_traj[:,0],r_traj[:,1])
plt.show()

r_traj[0] = np.array([2.0,0.0])
v_traj[0] = np.array([0.0,0.1/m])

for i in range(T-1):
    results = propagate_frog(dt, r_traj[i], v_traj[i], m, G,M)
    r_traj[i+1] = results[0]
    v_traj[i+1] = results[1]
    pot_traj[i] = get_potential(G,m,M,r_traj[i])
    kin_traj[i] = 0.5*m*(np.linalg.norm(v_traj[i])**2)
    total_traj[i] = pot_traj[i] + kin_traj[i]


plt.plot(r_traj[:,0],r_traj[:,1])
plt.show()
plt.plot(pot_traj)
plt.plot(kin_traj)
plt.plot(total_traj)
plt.show()
