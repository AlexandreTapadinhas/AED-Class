import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('times_final.csv')

plt.plot(df['P'], df['A'], '-o')
plt.xlabel('Tamanho do array')
plt.ylabel('Tempo de execução do Algoritmo A')
#plt.show()

plt.plot(df['P'], df['B'], '-o')
plt.xlabel('Tamanho do array')
plt.ylabel('Tempo de execução do Algoritmo B')
#plt.show()


plt.plot(df['P'], df['C'], '-o')
plt.xlabel('Tamanho do array')
plt.ylabel('Tempo de execução do Algoritmo C')
plt.show()
