import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np

# Array decleration for the different variables:
Ohm_a = []
Ohm_b = []
Ohm_tot = []
S_a = []
S_b = []
S_tot = []

# Multiplicity formula:
def Multiplicity(N, q):
    M = (m.factorial(q + N - 1))/((m.factorial(q))*(m.factorial(N-1)))
    return M
    

# Scenario 1 : NA = 100 and NB = 100
q_a = 0
q_b = 25 #q_total = 3 + 3 + 7 + 2 + 4 + 1 + 0 + 5 = 25
Ohm_a.clear()
Ohm_b.clear()

for i in range(0,26):
    Ohm_a.append(Multiplicity(100, q_a))
    Ohm_b.append(Multiplicity(100, q_b))
    q_a += 1
    q_b -= 1
    
Ohm_tot = np.multiply(Ohm_a, Ohm_b)

S_a = np.log(Ohm_a)
S_b = np.log(Ohm_b)
S_tot = np.log(Ohm_tot)

qA_graph = np.arange(0,26)

plt.scatter(qA_graph, S_a, color = 'blue', label = '$S_A$')
plt.scatter(qA_graph, S_b, color = 'orange', marker = 'x', label = '$S_B$')
plt.scatter(qA_graph, S_tot, color = 'green', marker = '+', label = '$S_{total}$')
plt.xlabel('qA')
plt.ylabel('Entropy in units of k')
plt.title('Graph of Entropy versus $q_A$ for $N_A = N_B = 100$')
plt.legend()

plt.show()


# Scenario 2 : NA = 100 and NB = 300
q_a = 0
q_b = 25
Ohm_a.clear()
Ohm_b.clear()
np.delete(Ohm_tot,0)
np.delete(S_a,0)
np.delete(S_b,0)
np.delete(S_tot,0)

for i in range(0,26):
    Ohm_a.append(Multiplicity(100, q_a))
    Ohm_b.append(Multiplicity(300, q_b))
    q_a += 1
    q_b -= 1
    
Ohm_tot = np.multiply(Ohm_a, Ohm_b)

S_a = np.log(Ohm_a)
S_b = np.log(Ohm_b)
S_tot = np.log(Ohm_tot)

plt.scatter(qA_graph, S_a, color = 'blue', label = '$S_A$')
plt.scatter(qA_graph, S_b, color = 'orange', marker = 'x', label = '$S_B$')
plt.scatter(qA_graph, S_tot, color = 'green', marker = '+', label = '$S_{total}$')
plt.xlabel('qA')
plt.ylabel('Entropy in units of k')
plt.title('Graph of Entropy versus $q_A$ for $N_A = 100$ and $N_B = 300$')
plt.legend()
plt.show()


q_a = 1
q_b = 25
T_A = []
T_B_100 = []
T_B_300 = []
T_Tot_1 = []
T_Tot_2 = []
k_eps = 8.617333262e-5/0.1

for i in range(0,25):
    T_A.append(1/(k_eps*np.log(1+(100/q_a))))
    T_B_100.append(1/(k_eps*np.log(1+(100/q_b))))
    T_B_300.append(1/(k_eps*np.log(1+(300/q_b))))
    q_a += 1
    q_b -= 1

T_Tot_1 = np.add(T_A,T_B_100)
T_Tot_2 = np.add(T_A,T_B_300)

qA_Temp = np.arange(1,26)

plt.scatter(qA_Temp, T_A, color = 'blue', label = '$T_A$')
plt.scatter(qA_Temp, T_B_100, color = 'orange', marker = 'x', label = '$T_B$')
plt.scatter(qA_Temp, T_Tot_1, color = 'green', marker = '+', label = '$T_{total}$')
plt.xlabel('qA')
plt.ylabel('Temperature (K)')
plt.title('Graph of Temperature versus $q_A$ for $N_A = N_B = 100$')
plt.legend()
plt.show()

plt.scatter(qA_Temp, T_A, color = 'blue', label = '$T_A$')
plt.scatter(qA_Temp, T_B_300, color = 'orange', marker = 'x', label = '$T_B$')
plt.scatter(qA_Temp, T_Tot_2, color = 'green', marker = '+', label = '$T_{total}$')
plt.xlabel('qA')
plt.ylabel('Temperature (K)')
plt.title('Graph of Temperature versus $q_A$ for $N_A = 100$ and $N_B = 300$')
plt.legend()
plt.show()
