import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(5)
n = 40
ram = np.random.choice([4, 6, 8, 12], n)
battery = np.random.choice([4000, 4500, 5000, 5500, 6000], n)
price = (ram * 1800 + battery * 0.9 + np.random.normal(0, 3000, n)).round(0)
rating = (3.5 + ram * 0.05 + np.random.normal(0, 0.25, n)).clip(3, 5).round(1)

pd.DataFrame({
    "price": price,
    "rating": rating,
    "RAM": ram,
    "battery_capacity": battery
}).to_csv("flipkart_mobiles.csv", index=False)

phones = pd.read_csv("flipkart_mobiles.csv")
corr = phones[["price", "rating", "RAM", "battery_capacity"]].corr()

sns.heatmap(corr, annot=True, cmap="RdYlGn", vmin=-1, vmax=1, center=0)
plt.title("Flipkart Mobile Phones - Correlation Heatmap")
plt.show()