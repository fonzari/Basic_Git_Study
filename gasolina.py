
import pandas as pd
import matplotlib.pyplot as plt

#  CSV 
df = pd.read_csv("gasolina.csv")

# PLOT
plt.figure(figsize=(10, 6))
plt.plot(df['dia'], df['venda'], marker='o', linestyle='-')
plt.xlabel('Dia', fontsize=12)
plt.ylabel('Preço da Gasolina (R$)', fontsize=12)
plt.title('Variação do Preço da Gasolina por Dia', fontsize=14)
plt.grid(axis='y', linestyle='--')
plt.show()

# SALVAR EM PNG
plt.savefig('gasolina.png')
