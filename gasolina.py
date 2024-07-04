
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gasolina.csv")

plt.figure(figsize=(10, 6))


plt.plot(df['dia'], df['venda'], marker='o', linestyle='-')

plt.xlabel('Day', fontsize=12)
plt.ylabel('Gasoline Price', fontsize=12)
plt.title('Gasoline Price Variation', fontsize=14)

plt.grid(axis='y', linestyle='--')

plt.savefig('gasolina.png')

plt.show()
